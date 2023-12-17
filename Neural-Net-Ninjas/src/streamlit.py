import streamlit as st
import requests
import pdfplumber

def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def main():
    st.title("PDF Question Answering App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.text("PDF Text:")
        st.text(pdf_text)

        question = st.text_input("Enter your question:")

        if st.button("Get Answer"):
            response = requests.post("http://127.0.0.1:5000/get_answer", data={"pdf_text": pdf_text, "question": question})
            answer = response.json().get("answer", "Error retrieving answer.")
            st.subheader("Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
