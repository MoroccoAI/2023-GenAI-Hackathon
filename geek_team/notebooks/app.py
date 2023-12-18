import subprocess

sub_p_res = subprocess.run(['pip', 'install', 'langchain', 'sentence-transformers', 'transformers', 'faiss-gpu', 'PyPDF2', 'torc'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print("pip install downloded ", sub_p_res)


command = 'CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python'

sub_p_res = subprocess.run(command, shell=True, check=True)

print("llama-cpp-python GPU downloaded ",sub_p_res)


from langchain.document_loaders.text import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager


from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from huggingface_hub import hf_hub_download
from langchain.llms import LlamaCpp

import time

import streamlit as st

#from PyPDF2 import PdfReader

# from google.colab import drive
# drive.mount('/content/drive')

loader = TextLoader("./drive/MyDrive/Colab Notebooks/hackathon_MoroccoAI/blog_data.txt")
pages = loader.load()

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

chunks_text = split_text(pages)

print("chunks")


# def Pdf_to_text(path) :
#     pdf_reader = PdfReader(path)

#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len
#         )
#     chunks = text_splitter.split_text(text=text)
#     return chunks

#chunks_pdf = Pdf_to_text("./drive/MyDrive/Colab Notebooks/hackathon_MoroccoAI/Doing-Business-Guide-Morocco.pdf")

#embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2') # machi top

docs_text = [doc.page_content for doc in chunks_text]

# final_chunks = []

# # for chunk in chunks_pdf :
# #   final_chunks.append(chunk)

# for chunk in docs_text :
#     final_chunks.append(chunk)

VectorStore = FAISS.from_texts(docs_text, embedding=embedding)

MODEL_ID = "TheBloke/Mistral-7B-OpenOrca-GGUF"
MODEL_BASENAME = "mistral-7b-openorca.Q4_K_M.gguf"

model_path = hf_hub_download(
            repo_id=MODEL_ID,
            filename=MODEL_BASENAME,
            resume_download=True,
        )

print("model_path : ", model_path)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


CONTEXT_WINDOW_SIZE = 1500
MAX_NEW_TOKENS = 2000
N_BATCH = 512
n_gpu_layers = 40
kwargs = {
          "model_path": model_path,
          "n_ctx": CONTEXT_WINDOW_SIZE,
          "max_tokens": MAX_NEW_TOKENS,
          "n_batch": N_BATCH,
          "n_gpu_layers": n_gpu_layers,
          "callback_manager": callback_manager,
          "verbose":True,
      }

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import LlamaCpp

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
max_tokens = 2000
# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,

    n_batch=n_batch,
    max_tokens= max_tokens,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

llm = LlamaCpp(**kwargs)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    input_key='question',
    output_key='answer'
)

# memory.clear()

qa = ConversationalRetrievalChain.from_llm(
    llm,
    chain_type="stuff",
    retriever=VectorStore.as_retriever(search_kwargs={"k": 5}),
    memory=memory,
    return_source_documents=True,
    verbose=False,
)

# start = time.time()
# res = qa(f"""
# I want to create my own company in morocco, give me steps to do that""")
# end = time.time()
# execution_time = end - start


#---------------------------------------------------------

import streamlit as st
import time


# App title
st.set_page_config(page_title="🤖💼 🇲🇦 Financial advisor is Here")

# Replicate Credentials
with st.sidebar:
    st.title('Mokawil.AI is Here 🤖💼 🇲🇦')
    st.markdown('🤖 an AI-powered advisor designed to assist founders (or anyone aspiring to start their own company) with various aspects of business in Morocco, including legal considerations, budget planning, available investors, and strategies for success.')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    if message["role"] == "user" :
      with st.chat_message(message["role"], avatar="user.png"):
          st.write(message["content"])
    else : 
      with st.chat_message(message["role"], avatar="logo.png"):
          st.write(message["content"])

def clear_chat_history():
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        input_key='question',
        output_key='answer'
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        chain_type="stuff",
        retriever=VectorStore.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        return_source_documents=True,
        verbose=False,
    )
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llm_response(prompt_input):
    res = qa(f'''{prompt_input}''')
    return res['answer']

# User-provided prompt
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="user.png"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
  with st.chat_message("assistant", avatar="logo.png"):
      with st.spinner("Thinking..."):
          response = generate_llm_response(st.session_state.messages[-1]["content"])
      placeholder = st.empty()
      full_response = ''
      for item in response:
          full_response += item
          placeholder.markdown(full_response)
          time.sleep(0.05)
      placeholder.markdown(full_response)
  message = {"role": "assistant", "content": full_response}
  st.session_state.messages.append(message)

# Example prompt
with st.sidebar : 
  st.title('Examples :')

def promptExample1():
    prompt = "how can I start my company in morocco?"
    st.session_state.messages.append({"role": "user", "content": prompt})

# Example prompt
def promptExample2():
    prompt = "What are some recommended cities for starting a business in finance"
    st.session_state.messages.append({"role": "user", "content": prompt})

# Example prompt
def promptExample3():
    prompt = "what is the estimate money I need for starting my company"
    st.session_state.messages.append({"role": "user", "content": prompt})


st.sidebar.button('how can I start my company in morocco?', on_click=promptExample1)
st.sidebar.button('What are some recommended cities for starting a business in finance', on_click=promptExample2)
st.sidebar.button('what is the estimate money I need for starting my company', on_click=promptExample3)


with st.sidebar:
    st.title('Disclaimer ⚠️:')
    st.markdown('may introduce false information')
    st.markdown('consult with a preofessionel advisor for more specific problems')
