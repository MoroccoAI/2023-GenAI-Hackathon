

# Eldians - VisionVista

## Abstract

### Background and Problem Statement:
Eldians' VisionVista project emerged from the Morocco AI 2023 hackathon, aiming to aid visually impaired individuals. The challenge was to design smart glasses capable of replacing visual functions by detecting surroundings. The project centered on using Language Models (LMs) to transform visual data into actionable information for the visually impaired.

### Impact and Proposed Solution:
The primary objective was to create smart glasses that describe surroundings through a combination of 3D object detection and language models. This solution intends to empower visually impaired individuals, providing real-time environmental descriptions and assisting in daily activities.

### Project Outcomes and Deliverables:
Expected outcomes involve refined prompt strategies, faster image processing, improved model responses, and integrating real-time object detection. The project aims to develop a prototype capable of smooth interaction and concise, context-aware responses.

## Team Members
- ZAOUG Imad
- EL BAHA Ali
- LOURARI Yahya

---



## Project Sections
This README summarizes the various phases and accomplishments of our project:

- **Introduction:** Provides context about the hackathon and project overview.
- **Version 0.1:** Details the initial model design, used models, tests conducted, results obtained, and limitations.
- **Version 0.2:** Highlights enhancements made, changes in models, conducted tests, results, and identified limitations.
- **Conclusion and Perspectives:** Offers a conclusion on the achieved milestones, along with future directions and unresolved issues.

You can find more details in the [report](https://github.com/Lourarhi-Yahya/2023-GenAI-Hackathon/blob/main/Eldians/Eldians_report_VisioVista.pdf)

---

## Getting Started

Follow these instructions to set up and run the VISIONVISTA system on your local machine.

### Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- [Hugging Face Transformers](https://github.com/huggingface/transformers) library
- [Streamlit](https://streamlit.io/) library
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library
- [pyttsx3](https://pypi.org/project/pyttsx3/) library
- [Matplotlib](https://matplotlib.org/) library
- [NumPy](https://numpy.org/) library
- [Pillow (PIL)](https://pillow.readthedocs.io/) library

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/Lourarhi-Yahya/Hackaton2023_GenAI
cd Hackaton2023_GenAI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run interface.py
```

4. Follow the on-screen instructions to upload an image and initiate a conversation.

## System Architecture

- `COMPUTER_Vision.py`: Contains the computer vision functions for object detection and depth estimation.
- `interface.py`: Implements the Streamlit interface and integrates the computer vision system with speech interaction.

## Speech Interaction

The system uses the Google Speech Recognition service to convert spoken words to text. Make sure you have a reliable internet connection for accurate speech recognition.

## Demos

[Demo](https://github.com/Lourarhi-Yahya/2023-GenAI-Hackathon/blob/main/Eldians/Demo_Eldians_Version_0.2.mp4) (Demo_Eldians_Version_0.2)

[Real time simulation](https://github.com/Lourarhi-Yahya/2023-GenAI-Hackathon/blob/main/Eldians/Real_time_demo_video.mp4) (Real_time_demo_video)

## Quality and Contributions

We welcome contributions to enhance VisionVista. If you encounter issues or have suggestions, feel free to open an [issue](https://github.com/Lourarhi-Yahya/2023-GenAI-Hackathon/blob/main/Eldians/issues) or submit a pull request.

Please follow these guidelines for contributing:

- Clearly describe the problem or enhancement.
- Provide sample code or steps to reproduce the issue.
- Ensure the code follows best practices and is well-documented.

## License

This project is licensed under the [MIT License](LICENSE.md).
