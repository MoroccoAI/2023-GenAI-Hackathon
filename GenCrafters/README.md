# ShifaChat

# Background and problem statement:

In the healthcare field, non-critical injuries such as minor bruises, cuts or sprains often lack immediate and reliable first-aid advice. Typically, these injuries, while not life-threatening, can cause discomfort or concern for individuals. The problem is compounded by the fact that such minor ailments aren't usually a priority in traditional medical settings, leading to delays in seeking professional advice. In addition, the vast and unstructured information available online can be overwhelming, often leading to confusion rather than clarity.

# Our Solution

ShifaChat is a healthcare chat assistant app that provides a comprehensive solution to the need for immediate and reliable first aid advice for non-critical injuries. The app addresses the common gap in professional advice for minor health concerns such as bruises, cuts or sprains, which are often not prioritized in traditional healthcare settings.

A key feature of ShifaChat is its multimodal and multilingual interface. Not only does the app allow users to upload images of their injuries for more nuanced analysis, it also supports audio input, allowing users to verbally describe their symptoms. This feature is particularly beneficial for those who prefer to express their health concerns verbally or find typing inconvenient.

In addition, ShifaChat's multilingual capabilities make it accessible to a diverse user base, breaking down language barriers that often impede access to quality healthcare information. By supporting multiple languages, ShifaChat ensures that users can receive medical advice in their preferred language, further personalizing the experience.

Combining these features with a knowledge base vetted by medical professionals ensures that the advice provided is specific, reliable and medically sound. By incorporating these advanced features, ShifaChat aims to not only streamline the management of minor health issues, but also reduce the reliance on unnecessary doctor visits. It provides an efficient, user-friendly and inclusive platform for health concerns, ultimately promoting improved self-care practices and increased health awareness among diverse communities.


# Workflow
<img width="2547" alt="shapes at 23-12-17 18 19 19" src="https://github.com/AhmedIdr/2023-GenAI-Hackathon/assets/31652778/8b9ad381-e218-4f9c-9fde-e12c560497b7">

---
When building the project, we had a goal of relying only on open-source and openly available models, which we achieved. The project consists of the following parts:

## 1. Automatic Speech Recognition:

This feature provides the ability to record and input your audio instead of text.

For this we used the *[SeamlessM4T V2 large](https://huggingface.co/facebook/seamless-m4t-v2-large)* model.

## 2. Text translation:

Since our knowledge base only contains English data, we decided to use translation to make the use of different languages possible.

Similar to ASR, the *[SeamlessM4T V2 large](https://huggingface.co/facebook/seamless-m4t-v2-large)* model was used.

## 3. Retrieval Augmented Generation:

To base the answers and suggestions to the user questions, we use retrieval augmented generation to base the answers of the LLM on the (doctor-vetted) knowledge base to be able to make factual suggestions and prevent the model from hallucinating.

For the purpose of this hackathon, we use the *[First Aid Recommendation](https://huggingface.co/datasets/badri55/First_aid__dataset)* dataset.

To encode the questions available in the dataset, we use the *[Bge v1.5 Large](https://huggingface.co/BAAI/bge-large-en-v1.5)* model.

The vectors were then indexed using the *[FAISS](https://github.com/facebookresearch/faiss)* library to enable semantic search and find similar questions to the user query and retrieve the related suggestions.

## 4. Vision Language Model:

Since the user has the ability to upload an image, we needed a vision language model to generate a description of the provided image. For this purpose, we use the *[LLava v1.5 13b](https://huggingface.co/liuhaotian/llava-v1.5-13b)* model.

## 5. Large Language Model:

To reason and generate suggestions based on the different inputs (User query/question, retrieved suggestions and the image description), we use a finetuned of the recently released Mixtral 8x7B model called *[dolphin-2.5-mixtral-8x7b ](https://huggingface.co/ehartford/dolphin-2.5-mixtral-8x7b)*. A system prompt was also included to instruct the model to come up with the correct answer.

## 6. Model Serving:

To serve the VLM and LLM, we used *[Ollama](https://ollama.ai/)* that serves the model in a quantized form and provides an easy-to-use local api.

We specifically used the docker container of ollama with different GPUs (llava on A6000 and dolphin-2.5-mixtral-8x7b on H100).

## 7. Fact Checking (ToDo):

To provide additional Internet sources to the suggestions, we tried using SerpAPI to perform a Google search and use the *[questions and answers](https://serpapi.com/google-questions-and-answers)* provided by Google to compare the suggestions and find similar ones and use the references.  Unfortunately, we have found that these questions and answers are not always available and have marked these features as todos for the future.
The UI was probably the hardest part, since we don't have that much experience in React but having a cool UI was also a goal of ours, which is why we kept pushing.

---
Notice: We chose not to utilize tools like LangChain and LlamaIndex as they tend to obscure the underlying processes, making it difficult to grasp what truly happens in the background. For us, it was crucial to have a clear understanding of the workflow within the pipeline to ensure a deeper comprehension of its operation.


# Demo Video

https://github.com/AhmedIdr/2023-GenAI-Hackathon/assets/31652778/95e1669d-12e1-4b04-966a-2bb6b9b4ae28

# Usage

The project was built in a manner that each part of the pipeline can be deployed as its own service. If you want to run the whole project you should:

- First, run encode_and_index.py file in the APIs folder.
- Then start all the provided APIs. You might need to change the ports of the different flask APIs, since, for our setup, each API was deployed in a separate docker container with a port forwarding.
- Deploy the VLM and the LLM by using ollama docker container.
First, you pull the docker image and start it.
```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
Then start the desired model with the following command:

```
docker exec -it ollama ollama run dolphin-2.5-mixtral-8x7b
```
After starting all the services, you can now start the User Interface in the UI/nextjs-multi-modal folder.

- First, you will need to run `npm install` to install the needed packages.
- And `npm run dev` to start the app.

! The app won't work out of the box since all the API calls in the UI will require adding the right APIs IP Addresses and ports.
! The whole project was deployed in our setup using multiple high-end GPUs, so it needs some heavy resources to run.

