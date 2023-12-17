import streamlit as st


st.title("Tahseen.ai --- تحسين")
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

st.divider()

st.header("Meet the team behind tahseen.ai")


st.subheader("Co-founders:")

st.write("""

KOUZMANE Fouad: Tech Lead BI @ Eviden | x-Deloitte

contact: fouadkouzmane@gmail.com

BOULAALA Hamza: Data Scientist @ SophiaGENETICS

contact: hamzaboulaalaop@gmail.com

""")

st.subheader("Our story and Why ?:")

st.write("""
We are **old INSEA** (Institut national de statistique et d'économie appliquée) schoolmates reunited in **Bordeaux**, hence our hackathon team name **BDX**.

We are both **passionate entrepreneurs** that love building exciting products that impact and create value for society.

That is why we decided to create tahseen.ai, in order to impact the upcoming generations by enabling teachers to level up their course materials and embrace generative AI
as a tool that will **enhance** their potential and not *replace* them.

Furthermore, we want to inspire students to dive deeper into AI and inspire their creativity and introduce them to a whole new learning experience.
""")

st.subheader("Thank you for reading this and meeting us !")

st.write("""
If you have any questions, feedback OR want to invest in us and tahseen.ai, feel free to contact us.

""")

st.divider()
fouad, hamza = st.columns(2)

with fouad:
  st.subheader("Fouad")
  st.image("/content/fouad_demo.png", use_column_width='auto')


with hamza:
  st.subheader("Hamza")
  st.image("/content/hamza_boulaala_demo.png")
