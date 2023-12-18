# Medical Tutor

## Created by

- [Hamza ES-SAMAALI](https://www.linkedin.com/in/hamza-es/)

## Problematic

In the realm of medical education, students face an uphill battle marked by the complexities of vast and dynamic study materials. Traditional study methods often fall short in catering to the specific needs of individual learners, leading to a lack of personalized guidance and a struggle to master the extensive curriculum. Furthermore, the growing demand for medical education, evident in the increasing enrollments globally, calls for innovative solutions to enhance the efficiency and effectiveness of exam preparation. 

## Proposal

'Medical Tutor' emerges as the solution to these challenges, offering a tailored approach to learning that leverages advanced technology to provide personalized study materials, generate relevant questions, and foster adaptive learning experiences for aspiring medical professionals.

## Impact

Medical Tutor have the potential to significantly impact the landscape of medical education by offering a tailored and adaptive learning experience. With its personalized study questions and efficient exam preparation features, the app empowers students to navigate the challenges of medical school with greater efficiency and confidence. 
Medical Tutor not only addresses the individual needs of learners but also contributes to the broader transformation of medical education methodologies. This tool has the potential to enhance comprehension and ultimately shape a more effective and accessible approach to medical education on a global scale.


## Key Features

The key features so far are:

1. **Document Analysis:** Upload and analyze course materials.

2. **Customized Question Generation:** Generate personalized study questions based on the content of uploaded document.

More features will be added later:  

3. **Adaptive Learning:**
   - Dynamically adapt question difficulty based on the user's performance and progress.
   - Provide targeted practice to reinforce weaker areas and challenge stronger ones.

4. **Feedback and Insights:**
   - Offer detailed feedback on user responses, highlighting correct answers and explaining incorrect ones.
   - Provide performance insights and analytics to track progress over time.

5. **Resource Integration:**
   - Allow integration with various file formats, including PDFs, Word documents, and presentations.
   - Support multiple courses and subjects, enabling comprehensive exam preparation.

## Technologies

- LangChain
- Mixtral 8x7b
- FAISS
- Streamlit

## Architecture

![Image](architecture.png)

## Demo

- [Deployed App](https://medicaltutor.streamlit.app/)
- [Video Demo](https://youtu.be/qFfjY2u_ruo)

## Instructions
- The app is deployed on Streamlit Community Cloud you can access it [here](https://medicaltutor.streamlit.app/).  

To run the app locally please follow these steps:
1. `git clone https://github.com/HaoES/Meditron-RAG.git`
2. `cd Meditron-RAG`
3. `pip install -r requirements.txt`
4. `streamlit run app.py`
