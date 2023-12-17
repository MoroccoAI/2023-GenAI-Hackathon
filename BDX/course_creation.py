import streamlit as st
from st_pages import Page, show_pages, add_page_title
from deep_translator import GoogleTranslator
from transformers import pipeline
from keras_cv.models import StableDiffusion
from PIL import Image
from streamlit_extras.app_logo import add_logo
import os
from transformers import VitsModel, AutoTokenizer
import torch
from IPython.display import Audio
import scipy
import time
from zipfile import ZipFile
from transformers import AutoTokenizer, AutoModelWithLMHead
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

from diffusers import DiffusionPipeline


st.set_page_config(page_title="Tahseen.ai --- تحسين",
                   page_icon="robot_face",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.sidebar.image("/content/logo.png")


css = f'''
        <style>

            .stApp {{
              background-color:#f9f5f2

            }}
            .stTextArea textarea{{
            border: 3px solid #ff914d
              }}
            .stApp > header {{
                background-color: transparent;
            }}
            [data-testid=stSidebar]  {{
            background-color: #E6E0DC ;
            color: white;
            }}
        </style>
        '''
st.markdown(css, unsafe_allow_html=True)




st.title("Tahseen.ai --- تحسين")

#@st.cache_resource to cache methods instead of loading them each time


# st.session_state["someobject"] = someobject

st.divider()


st.expander("""Tahseen.ai is your assistant in creating your content for courses using cutting edge AI in just one click.

  """
)

# add Tahseen.ai desciption here


### models

def get_summary(text, tokenizer, model, device="cpu", num_beams=2):
    if len(text.strip()) < 50:
        print("Please provide more longer text")

    text = "summarize: <paragraph> " + " <paragraph> ".join([ s.strip() for s in sent_tokenize(text) if s.strip() != ""]) + " </s>"
    text = text.strip().replace("\n","")

    tokenized_text = tokenizer.encode(text, return_tensors="pt").to(device)

    summary_ids = model.generate(
            tokenized_text,
            max_length=512,
            num_beams=num_beams,
            repetition_penalty=1.5,
            length_penalty=1.0,
            early_stopping=True
    )

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return [ s.strip() for s in output.split("<hl>") if s.strip() != "" ]

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

if 'loaded_models' not in st.session_state:
  with st.spinner("Preparing workspace"):
    st.session_state["models"]={}
    st.session_state["models"].update({"translator_eng": GoogleTranslator(source='auto', target='en')})
    st.session_state["models"].update({"translator_ar": GoogleTranslator(source='auto', target='ar')})
    st.session_state["models"].update({"summarizer": pipeline("summarization", model="facebook/bart-large-cnn")})
    st.session_state["models"].update({"model_image_hf": DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
                                                                                            torch_dtype=torch.float16,
                                                                                            use_safetensors=True,
                                                                                            variant="fp16",
                                                                                            seed=None)})
    st.session_state["models"].update({"model_audio": VitsModel.from_pretrained("facebook/mms-tts-ara")})
    st.session_state["models"].update({"audio_tokenizer": AutoTokenizer.from_pretrained("facebook/mms-tts-ara")})
    st.session_state["models"].update({"bulletp_tokenizer":  AutoTokenizer.from_pretrained("marefa-nlp/summarization-arabic-english-news")})
    st.session_state["models"].update({"bulletp_model":  AutoModelWithLMHead.from_pretrained("marefa-nlp/summarization-arabic-english-news").to(device)})

    st.session_state['loaded_models'] = True


if st.session_state['loaded_models'] :
  st.write("Workspace is ready !!")

full_text = st.text_area('Text in arabic', ' ')
batch_size = st.sidebar.number_input(label="Number of images based on the summary",value=1, placeholder="Insert an integer", min_value=1, max_value=10, step=1)

# Generate
button_enhance = st.button('Generate')

progress_text = "Generating content .......... تحضير المحتوى"
percent_complete = 0

def log_progress(my_bar, percent_complete, progress_text):
    time.sleep(0.01)
    my_bar.progress(percent_complete, text=progress_text)


st.header("Content creation")

st.session_state["outputs"] = {}

if button_enhance:
    my_bar = st.progress(percent_complete, text=progress_text)
    with st.spinner(text="This may take a moment..."):
      log_progress(my_bar, percent_complete+10, progress_text)
      translator_eng = st.session_state["models"]["translator_eng"]
      log_progress(my_bar, percent_complete+10*2, progress_text)
      translator_ar = st.session_state["models"]["translator_ar"]
      log_progress(my_bar, percent_complete+10*3, progress_text)
      summarizer = st.session_state["models"]["summarizer"]
      log_progress(my_bar, percent_complete+10*5, progress_text)
      model_image_hf = st.session_state["models"]["model_image_hf"]
      log_progress(my_bar, percent_complete+10*6, progress_text)
      tokenizer = st.session_state["models"]["audio_tokenizer"]
      log_progress(my_bar, percent_complete+10*7, progress_text)
      bulletp_tokenizer = st.session_state["models"]["bulletp_tokenizer"]
      log_progress(my_bar, percent_complete+10*8, progress_text)
      bulletp_model = st.session_state["models"]["bulletp_model"]
      log_progress(my_bar, percent_complete+10*9, progress_text)
      model_audio = st.session_state["models"]["model_audio"]
      model_image_hf.to("cuda")
      log_progress(my_bar, 100, progress_text)

    # Use any translator you like, in this example GoogleTranslator

    st.header("Arabic summary ----- ملخص عربي")

    with st.spinner("Generating summary"):
      translated_input = translator_eng.translate(full_text)
      st.session_state["outputs"]["translated_input_eng"] = translated_input

      # summarization
      eng_summary = summarizer(translated_input, max_length=500, min_length=30, do_sample=False)
      eng_summary_text = eng_summary[0]["summary_text"]
      st.session_state["outputs"]["eng_summary_text"] = eng_summary_text

      # ARABIC translator
      arabic_summary = translator_ar.translate(eng_summary[0]["summary_text"])
      st.text_area(label ="Arabic summary:",value=arabic_summary, height=50)
      st.session_state["outputs"]["arabic_summary"] = arabic_summary

    #st.write(arabic_summary)

    st.header("Bullet points ---- نقاط مهمة")
    with st.spinner("Generating bullet points"):
      hls = get_summary(full_text, bulletp_tokenizer, bulletp_model, device)

      st.write("Bullet points:")
      for hl in hls:
        st.write(f"- {hl}")
    st.session_state["outputs"]["bullet_points"] = hls

    ## SPEECH model
    st.header("Audio content --- المحتوى الصوتي")
    with st.spinner("Generationg audio content"):
      text = arabic_summary
      inputs = tokenizer(text, return_tensors="pt")

      with torch.no_grad():
          output = model_audio(**inputs).waveform


      scipy.io.wavfile.write("summary_narrated.wav", rate=model_audio.config.sampling_rate,
      data=output.cpu().float().numpy().T)
      st.subheader("Summary narration:")
      st.audio("/content/summary_narrated.wav", format='audiowav')


    # IMAGE GENERATION MODEL
    st.header("Image generation --- خلق الصور")

    images_list=[]
    with st.spinner('Generating images'):
      for i in range(batch_size):
        summary_image = model_image_hf(prompt=eng_summary_text).images[0]
        images_list.append(summary_image)
    
    st.subheader("Images generated based on the summary")
    for img in images_list:
      st.image(img, caption=eng_summary_text)
      time.sleep(5)
    st.session_state["outputs"]["images_list"] = images_list

    # images from bullet points
    images_log =[]
    st.subheader("Images generated based on the bullet points")

    with st.spinner("Generating images"):
      for prompt_ar in hls:
        prompt = translator_eng.translate(prompt_ar)
        images=model_image_hf(prompt=prompt).images[0]
        st.image(images, caption=prompt)
        images_log.append(images)

    st.success('Content generation Done !')
    st.session_state["outputs"]["bullet_points_img"] = images_log



  # Create a ZipFile Object
  #  download_button = st.checkbox('Download content')
  #  downloading_path = "./outputs/"
  #  if not os.path.exists(downloading_path):
  #    os.makedirs(downloading_path)
  #    st.success("Created folder successfuly")

   # if download_button:
    #  with st.spinner("downloading content"):
    #    with open('{downloading_path}/text_output.txt', 'w') as f:
    #      f.write("Arabic summary")
    #      f.write('\n')
    #      f.write(arabic_summary)
    #      f.write("Bullet points in arabic")
    #      f.write('\n')
    #      for bp in st.session_state["outputs"]["bullet_points"]:
    #        f.write(bp)
    #        f.write('\n')
    #      f.write('\n')
    #    f.close()
    #    for i, value in enumerate(images_list+images_log):
    #        value.save(f"{downloading_path}/image_{i}.png")
    #    scipy.io.wavfile.write("{downloading_path}/summary_narrated.wav",
    #                            rate=model_audio.config.sampling_rate,
    #                            data=output.cpu().float().numpy().T)
   
