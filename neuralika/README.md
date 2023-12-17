# genAI Hackathon-2023 - Project Tig-mi

We extend our sincere gratitude to Morocco AI 2023 for organizing the one-week AI hackathon.

![Morocco AI Logo](https://morocco.ai/wp-content/uploads/2020/03/MoroccoAI_Logo.png)

## 👋 Introduction

Welcome to our AI-powered generative interior design project, Tig-mi, where we explore the beauty of Moroccan culture through innovative AI techniques!

![Project Logo](./imgs/logo.jpg)

## Abstract

### Background and Problem Statement

Our project addresses the challenge of infusing Moroccan style into interior design images. Traditional Moroccan aesthetics are rich in patterns, colors, and textures, and we aim to seamlessly integrate them into modern interior designs.

### Impact and Proposed Solution

The potential impact of our solution lies in creating visually appealing and culturally infused interior designs. We leverage AI, combining image captioning, prompt engineering, user customization, and advanced image generation models to achieve this fusion.

### Project Outcomes and Deliverables

- AI-powered generative interior design combining Moroccan aesthetics and modern innovation.
- Integration of user customization for personalized designs.
- A demonstration featuring three distinct images transformed with a Moroccan touch.

## 📝 Description

Our AI-powered generative interior design project is an exciting fusion of traditional Moroccan aesthetics and modern technological innovation. By leveraging the power of AI, we seamlessly integrate intricate Moroccan patterns, vibrant colors, and luxurious textures into designs that prioritize functionality and practicality.

![Project Architecture](./imgs/architecture.png)

Our project consists of five main steps:

1. **Image Captioning:** Utilizing [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) to generate a description of the input image.
2. **Prompt Engineering:** Combining generated descriptions with Moroccan keywords and user style preferences.
3. **User Customization:** Allowing users to further customize content through input.
4. **Image Generation:** Using [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) to generate a new image incorporating original features, custom elements, and enriched description.
5. **Video Creation:** Utilizing [stability-ai/stable-video-diffusion](https://replicate.com/stability-ai/stable-video-diffusion) for specialized video creation using the generated image.

![Application Screenshot](./imgs/app_screenshot.png)

## 🚀 Installation 

To install the required packages, run the following command:

```bash
pip install -r requirements.txt


## 💻 Usage

To run the project, run the following command:

```bash
python main.py
```

![demonstration video](./imgs/4_video.gif)

## 👨‍💻 Team Members 

* [Wassim EL BAKKOURI](https://www.linkedin.com/in/wassim-elbakkouri/)
* [Ihssane Aoune](https://www.linkedin.com/in/ihssane-aoune-a911a9231/)
* [Fatima Zahra Zeghli](https://www.linkedin.com/in/fatima-zahra-zeghli-2b3715216/)
 
 
