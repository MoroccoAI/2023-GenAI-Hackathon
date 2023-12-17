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

st.header("Course Creation")
with st.expander("See explanation"):
  st.write(""" This content was created in the content creation space before to showcase the student page
  """)

st.subheader("Hello students ! This is your dedicated area to view your teachers course !")


st.divider()

text_column, image_column = st.columns(2)

with text_column:
   st.subheader("Summary of the course")
   st.write(st.session_state["outputs"]["arabic_summary"])
   st.write("Summary narration")
   st.audio("/content/summary_narrated.wav", format='audiowav')

   st.write("**important information about the course:**")
   for bp in st.session_state["outputs"]["bullet_points"]:
      st.write(bp)

with image_column:
    st.subheader("Course related images")
    for img in st.session_state["outputs"]["images_list"]:
      st.image(img)

    for img in st.session_state["outputs"]["bullet_points_img"]:
      st.image(img)



