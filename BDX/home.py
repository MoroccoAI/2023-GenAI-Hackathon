import streamlit as st
from st_pages import Page, show_pages, add_page_title
from deep_translator import GoogleTranslator
from transformers import pipeline
from keras_cv.models import StableDiffusion
from PIL import Image
from streamlit_extras.app_logo import add_logo

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

# Setup of page names, just add a page path and it's name and icon
show_pages(
            [
                Page("home.py", "Home","🏠"),
                Page("course_creation.py", "Course creation", "⚙️"),
                Page("course.py", "Course content" , "📚"),
                Page("about_us.py", "About us", "😊")
            ]
        )

st.title("Tahseen.ai --- تحسين")

st.header("Welcome to Tahseen.ai ! your all in one platform for AI course creation")

st.expander("""
    Home page to describe what our services are and what to expect from the app.
  """
)

with st.expander("What is Tahseen.ai"):
    st.write("""
          Tahseen.ai is an AI powered toolkit that helps teachers generate engaging materials such as images,
          voice-over and text summary to increase student engagement and retention.
    """)


st.divider()

st.subheader("For teachers:")

st.write("""
**course creation:** With just one click you can generate content to be used as part of your course material.

""")

st.divider()

st.subheader("For Students:")
st.write("""
**course content:** You can view your course created by teachers in your school.
""")

st.divider()

st.subheader("Worflow")

st.markdown("""This is a logigramme that could help you understand our workflow. **BUT IF YOU ARE ONLY INTERESTED IN USING/TESTING THE PRODUCT THEN SWITCH TO COURSE CREATION ON THE LEFT!!**

**Your content is only ONE click away !**
""")

st.image("/content/tahseenAI workflow testing v3.png")
