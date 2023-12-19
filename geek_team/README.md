![image](https://github.com/QoutiOussama13/VentureBuddy/assets/81428754/6830aec7-5624-4d15-a3df-f0c2c39bf9f0)
# Mokawil .AI 🤖💼🇲🇦



## Problem
Starting and managing a business in Morocco is challenging for entrepreneurs and aspiring business owners due to a lack of access to reliable information. Many struggle with the complexities of setting up a company, understanding tax requirements, and grasping Morocco-specific business terminology.
[Business failures in Morcco skyrocketed in 2022, rising by 17.4% compared to 2021.](https://www.moroccoworldnews.com/2023/01/353639/more-than-12-000-moroccan-businesses-failed-in-2022)

## Intorducing Mokawil.AI

Mokawil .AI is the first-of-its-kind GenAI-powered chatbot designed to assist entrepreneurs and aspiring entrepreneurs in starting their businesses in Morocco. It has access to specific information covering everything from creating a company, running it, understanding when and how much to pay taxes, business terminology in Morocco, and much more.


## Approach:

We utilized the Retrieval-Augmented Generation (RAG) technique to enhance the accuracy and reliability of our generative AI models. RAG optimizes the output of a large language model by referencing an authoritative knowledge base outside of its training data sources before generating a response.

The main tool we employed for making the RAG is [Langchain 🦜️⛓️](https://python.langchain.com/docs/get_started/introduction) for performence and simplicity .

### Phase 1: Data Collection and Embedding
1. **Data Collection:**
   - Gathered detailed blogs on entrepreneurship,taxes,and everything related to starting a company from  [BHAdviser](https://bhadviser.org/blog/).

2. **Embedding:**
   - Utilized a model from [Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) to transform data into vector representation.

3. **Vector Storage:**
   - Stored embeddings in the vector database [FAISS](https://ai.meta.com/tools/faiss/).

### Phase 2: User Interaction
1. **User Interaction:**
   - Users input prompts through the [Streamlit](https://streamlit.io/) interface.

2. **Prompt Embedding:**
   - Embedded user prompts using the same model used for data embedding.

3. **Similarity Search:**
   - Compared embedded user prompts with vector database data to find the best match.

### Phase 3: Large Language Model (LLM)
1. **LLM Selection:**
   - Utilized the [Mistral-7B-OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca) language model, incorporating [Q4 quantization](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF).

2. **Answers Generation:**
   - Fed results of similarity search to the LLM to generate answers based on user-specific needs and available information the answer are also saved in chat memroy to make use of them later .

3. **User Interface (UI):**
   - Presented answers in the Streamlit UI for user consumption.

**Global Architechtures**

![image](https://github.com/QoutiOussama13/VentureBuddy/assets/81428754/38516fea-5575-4791-af32-c1546035e96d)

# Instructions

To run the Mokawil .AI application, follow these steps:

1. **Open Google Colab:**
   - Access Google Colab using your preferred web browser.

2. **Install Requirements:**
   - Inside the Colab environment, install the necessary requirements. You can do this by running the following command in a code cell:
     ```python
     !pip install -r requirements.txt
     ```

3. **Run the Notebook:**
   - Open the notebook named "Rag financial advisor GPU.ipynb" in the Colab environment.
   - Execute the cells in the notebook to run the application.

Alternatively, you can explore a demo of the application directly on Hugging Face :
[Geek Team - Hugging Face](https://huggingface.co/spaces/MahmoudRox/Geek_team) 
*Note* : it takes time for generation for low ressouce

## Demo

![Geek_Team_-_a_Hugging_Face_Space_by_MahmoudRox_-_Google_Chrome_2023-12-18_14-32-56](https://github.com/QoutiOussama13/VentureBuddy/assets/81428754/fc22cd13-b0a5-49fe-9507-81e1a6adda6e)
![demo2](https://github.com/QoutiOussama13/VentureBuddy/assets/81428754/1a3a141b-7194-4193-b51c-440fcf840d8f)



## Future work
we plan on making Mokawil.AI more advanced and more helapful for the users by making it :

- **Personalized Responses:**
  - Provied tailord responses based on user-specific information.

- **Multilingual Support:**
  - to be Capable of understanding and responding in multiple languages.

- **Notification System:**
  - Sends notifications for important deadlines to keep users informed.

- **Versatile Input Support:**
  - Accepts text, audio, and document inputs for flexibility.

- **Financial Document Analysis:**
  - Analyzes financial documents to provide insightful information.

- **And Much More...**

![image](https://github.com/QoutiOussama13/VentureBuddy/assets/81428754/7cc69454-689a-47ef-9e24-2244bf819eca)


## Geek Team 

- [Oussama Qouti](https://www.linkedin.com/in/oussama-qouti-105bb820a/)
- [Mahmoud Bidry](https://www.linkedin.com/in/mahmoudbidry/)

