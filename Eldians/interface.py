

import google.generativeai as genai 
import streamlit as st
import tempfile
import os
import pandas as pd
import time
import speech_recognition as sr
import pyttsx3 
from COMPUTER_Vision import dimension_reducing, object_detection, propmpt, image_size ,reduce_image_quality



# Set the flag to indicate whether the initial explanation has been given
genai.configure(api_key='AIzaSyDE2osAYDuqBrX8p82HRUY9TXieQkl4qoo')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
prompt_1 = '''
Objective: To develop a high-performance model for guiding blind people using glasses equipped with cameras capable of scanning the environment. The model must detect objects using an object detection model and estimate the distance to these objects using a depth estimation model. The object detection and depth data will be supplied to the language model via a question or request from the person. The glasses are also equipped with models for converting speech into text and vice versa, to facilitate auditory interaction. The model must be able to analyze input data, provide clear and rapid responses, and virtually replace the person's eyes, informing about elements of the environment or answering questions. Depth matrices provide information on the distance of each pixel in the image. Object detection provides detailed information on the objects present, their type, position and depth. To answer questions such as the presence of obstacles on the left, a reduced depth matrix is used, averaged over blocks to simplify analysis. This information will be used to respond to the person's specific requests and maintain a fluid conversation, even if not directly related to their immediate environment.
Prompt :
Image size: (X*Y) - Example: (1280*960)
Reduced depth matrix: The initial dimension of the matrix was equal to the image dimension, so each coefficient in the depth matrix represents the depth of the pixel in the image. After reduction, the result is 64 regions.
Analysis required: The region x=1, y=1 represents the average of pixels between x1=0 and x2=X/8 and y=0 and y=Y/8. In general, the region x=k and y=s represents the average of pixels between x1=(k-1)*X/8 and x2=k*X/8 and y=(k-1)*Y/8 and y=k*Y/8. Example: [[2.92, 3.51, 3.48, 3.75, 3.37, 2.97, 3.02, 3.31], [1.87, 3.20, 4.07, 4.59, 4.26, 3.94, 3. 68, 3.68], [1.77, 3.75, 6.03, 6.51, 6.07, 6.09, 6.65, 4.28], [1.72, 3.99, 6.52, 5.86, 5.83, 5.38, 7.93, 4. 37], [1.72, 2.57, 4.04, 4.85, 4.86, 4.83, 4.55, 3.45], [1.78, 2.72, 4.05, 3.99, 3.71, 3.44, 3.50, 3. 32], [1.87, 2.64, 3.38, 3.32, 3.21, 3.21, 3.25, 3.16], [1.94, 2.46, 2.57, 2.54, 2.52, 2.51, 2.51, 2.53]]
Detected objects: In this section, you'll find the names of the various objects detected, along with their relative position in the shape image (x,y,z).2*X), (ymin+ymax)/(2*Y)). If (xmin+xmax)/(2*X) < 0.5, the object is on the left. If (xmin+xmax)/(2*X) > 0.5, the object is on the right. If (xmin+xmax)/(2*X) is close to 0.5, the project is in the middle. If (ymin+ymax)/(2*X) < 0.5, the object is at the top. If (xmin+xmax)/(2*X) > 0.5, the object is at the bottom. If (xmin+xmax)/(2*X) is close to 0.5, the project is in the middle. (The question of up and down is not important if depth > 5). The depth shows how far the object is from the glasses. If depth < 2, the object is close. If 2 < depth < 8, the object is in the middle. If 8 < depth, object is far away.
Analysis required: the user's position is (0,0,0), so to understand whether the object's position is to the left or right you rely on the sign of x, to understand whether the object's position is up or down you rely on the sign of y, and for the object's distance you rely on the value of z.
Examples: "Chair" at position (256.59, 485.54, 4.68).

Asks: "Are there any people next to me?"
Completion: "No, there are no people. However, pay attention to your left, as the distance in the first region of the depth matrix indicates a proximity between 1.7 and 2.9." Assist the blind person (if understood, answer with "let's get started").
note that : 
-you should answer directly with the response without details the information given before are just to help you understand the environement
-Summarize your answer in 2 to 4 sentences at max
-if the question is not related to the given data try to answer him kindly and maintain a proper conversation especially that the user is a blind person but keep your answers short ( max 5 sentences) 
-use an easy vocabulary that can be understandable by an average person (a person that doesn't understand technical words)
-if you couldn't answer say it clearly
'''

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "english" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1.0)
    engine.say(command)
    engine.runAndWait()
def main():
    st.title("Eldians")
    initial_explanation_given = False
    # Add file uploader for images
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Save the uploaded image to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name
        image_path=reduce_image_quality(image_path=image_path)
        S = image_size(image_path)
        A1, B = object_detection(image_path)
        C = dimension_reducing(B)

        if not initial_explanation_given:
            # If the initial explanation has not been given, provide it and set the flag to True
            response = chat.send_message(prompt_1)
            initial_explanation_given = True
            st.text("Ready")
        # Button to start the conversation
        if st.button("Start Conversation"):
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                st.text("Listening for speech input...")
                # Asking if the user wants to continue the conversation
                stop_button = st.button("Stop Conversation")

                while True:  # Infinite loop for the conversation
                    try:
                        # Record audio
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2, language="en-US")  # Recognizing speech in English
                        MyText = MyText.lower()

                        # Displaying vocal input on the interface
                        st.text(f"Vocal Command: {MyText}")

                        # Generating response based on vocal command
                        response = chat.send_message(propmpt(S, A1, C, MyText))
                        response = response.text
                        response = response.replace('*','')
                        response = response.replace('-','')
                        # Displaying the response
                        st.text(f"Response: {response}")

                        # Speaking the response
                        SpeakText(response)

                        if stop_button:
                            break  # Exiting the loop if the user stops the conversation

                    except sr.UnknownValueError:
                        st.text("Sorry, I couldn't understand the speech. Please try again.")
                    except sr.RequestError:
                        st.text("There was an issue with the Google Speech Recognition service. Please check your internet connection or try again later.")

        # Closing and deleting the temporary file
        temp_file.close()
        os.unlink(image_path)
 
if __name__ == "__main__":
    main()