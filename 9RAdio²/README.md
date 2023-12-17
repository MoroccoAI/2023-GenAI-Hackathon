![image](https://github.com/FZ-N/2023-GenAI-Hackathon/assets/41304333/3b6da154-e30a-4730-b8dc-097f3638e8ba)

# 9RAdio²
Introduces an AI-assisted radiological diagnosis accelerator, designed to revolutionize the patient journey in medical imaging.

**Background and Problem Statement:**

Doctors may request various types of medical imaging studies (such as radiology) depending on the patient's symptoms, medical history, and the suspected or diagnosed medical condition.  These imaging studies provide valuable information about the internal structures of the body and help doctors visualize and identify abnormalities or diseases. 

In Morocco, accessing radiological services, particularly within the public sector, often involves prolonged waiting times for both scheduling appointments and receiving results. Subsequently, obtaining an appointment with a healthcare professional can also be time-consuming. This delay in the entire process, from requesting a medical imaging study to consulting with a doctor, poses challenges for timely healthcare delivery.

The waiting period between undergoing a radiological examination and the subsequent consultation with a doctor is often a sensitive and anxious time for patients who are eager to understand their health status. Recognizing this, the project aims to address these concerns by leveraging a user-friendly Web application. 

It's important to emphasize that the primary goal is to assist doctors rather than replace them. This approach can also allow patients to receive preliminary information that can be confirmed and refined during subsequent consultations with healthcare professionals. 


**Impact and Proposed Solution:**

The AI assistant swiftly analyzes and segments radiological images. Real-time insights are generated, providing a preliminary assessment of the
images, including indications of normalcy or potential abnormalities. Armed with AI-assisted insights, the doctor can conduct a more focused and
informed discussion with the patient. With quicker access to diagnostic information, the doctor can promptly devise a targeted treatment plan.


**Project Outcomes and Deliverables:**

1-Code for GenAI  Pix2Pix that generates masks of chest x-ray images.

2-Code of fine-tuned ViT on the Chest X-ray dataset.

3- Code for Flask to  deploy web app where user can upload a chest image and get the segmentation as well as the type (normal or not).

**Instructions:**

Using the Flask API it's possible to deploy the model.

**Ressources:**

-Dataset:

https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels

or in google drive if you wanna run code in colab:
https://drive.google.com/drive/folders/1nuy_78-1oHqfw1CFgIs9kTFxwU7PNf8n?usp=sharing

-Code:

https://www.kaggle.com/code/tapliershiru/pix2pix-image-to-image-translation-tensorflow

https://thepythoncode.com/article/finetune-vit-for-image-classification-using-transformers-in-python

https://github.com/krishnaik06/Deployment-Deep-Learning-Model/blob/master/app.py
link for saved ViT model: https://drive.google.com/file/d/17n_NdO9Qp040anIVOfx96ZTwwJ_OmCHX/view?usp=sharing
For the Flask structure: https://drive.google.com/drive/folders/1QbAAbmcKbfjW_ksCNgHzMdiWPpvcdupI?usp=sharing
