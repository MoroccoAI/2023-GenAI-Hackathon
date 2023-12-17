import streamlit as st
from streamlit_modal import Modal
from codify import generate_response
from gradio_client import Client
import uuid
from retieve_student_chat import evaluate_student



def codify(role, username="", task_id=""):
    st.title(f"Codify - {role}")

    # Clear chat history when the role is changed
    if st.session_state.get("current_role") != role:
        st.session_state.current_role = role
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can I help you", key=role):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # For student case
        if role == "Student Assistant":
            response = generate_response(filtered_input(prompt), task_id, username)

        # For teacher case
        else:
            client = Client("https://ise-uiuc-magicoder-s-ds-6-7b.hf.space/--replicas/dccwp/")
            response = client.predict(
                    prompt,
                    0,	    # Temperature
                    2048,	# Max Tokens
		            api_name="/evaluate_magicoder"
            )
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)


# Add a new function for the Evaluation page
def evaluate(evaluation):
    st.title("Codify - Evaluation")
    
    if not evaluation:
        st.markdown("### Student didn't take this task!")
    elif evaluation[0] == "NONE":
        st.markdown("No student entered!")
    else:
        st.markdown(f"{evaluation}")

def user_guide():
    st.write("## User Guide:")
    st.write("To navigate through the different section, please click on the ```selectbox``` in the sidebar under the title **Navigation**.")
    st.write("### For the student part:")
    st.write("1. First, make sure to supply a ```Username``` and a ```Task ID``` as these will be used to identify the user with the task he worked on.")
    st.write("2. Now, you can engage in a conversation with codify. You can start with the prompts given at the sidebar.")
    st.write("3. Note that the responses might take a bit of time to be generated.")

    st.write("### For the teacher part:")
    st.write("You don't need to supply any parameters. You can directly start engaging in a conversation with codify. Fee free to use the prompts examples given.")


    st.write("### For the evaluation part.")
    st.write("Please use the ```Username``` and the ```Task ID``` you used to authenticate as a student.")

def main():
    PAGES = {
        "user Guide": user_guide,
        "Student Assistant": codify,
        "Teacher Assistant": codify,
        "Evaluation": evaluate,
    }

    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Select Feature", list(PAGES.keys()))

    print(choice)
    examples = []
    if choice == "Student Assistant":
        st.sidebar.markdown("#### !!! Please Enters Details Bellow !!!")

        username = st.sidebar.text_input("Enter Username:", placeholder="Mohamed").lower()
        task_id = st.sidebar.text_input("Enter Task ID:", placeholder="task_123").lower()
        # Check authentication on button click

        st.sidebar.markdown("### Examples of Prompts:")
        examples = [
            "How do I solve a Python error?", 
            "Explain the concept of object-oriented programming.", 
            "I need assistance with loops. Can you provide guidance?",
            "Write me a program that adds a list of integers passed on the command line."
        ]

        codify("Student Assistant", username, task_id)

    elif choice == "Evaluation":
        username = st.sidebar.text_input("Enter Student Name:", placeholder="Mohamed").lower()
        task_id = st.sidebar.text_input("Enter Task ID:", placeholder="task_123").lower()

        # Add button to sidebar to update chat on the evaluation page
        if st.sidebar.button("Update Chat"):
            st.rerun()
        
        if task_id != "" and user_guide != "":
            chat = evaluate_student(f"{task_id}.{username}")
            evaluate(chat)
        else:
            evaluate(["NONE"])

    elif choice == "Teacher Assistant":
        st.sidebar.markdown("### Examples of Prompts:")
        examples = [
            "Generate a Python coding assignment for beginners involving loops and conditionals.", 
            "Generate multiple-choice questions on data structures in C.",
            "Generate a real-world scenario where students can apply their knowledge of algorithms and data structures."
        ]

        codify("Teacher Assistant")

    else:
        user_guide()

    for example in examples:
       st.sidebar.markdown(example)


def filtered_input(user_input):
    full_code_intents = ["full code", "complete solution", "entire code", "give me code", "provide code"]

    if any(intent in user_input.lower() for intent in full_code_intents):
        " ".join([user_input, "Please, don't give me the full good encourage me to solve the problem myself."])
        return user_input
    return user_input


if __name__ == "__main__":
    main()