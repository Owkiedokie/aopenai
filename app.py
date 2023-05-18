import streamlit as st
import openai

# Set up the OpenAI API
openai.api_key = st.secrets["api_key"]

# Title of the app
st.title("C++ Code Generator")

# User input for the programming task
task = st.text_input("Enter the programming task:")

# Generate C++ code using OpenAI's GPT-3.5 model
def generate_code(task):
    prompt = f"Task: {task}\n\n```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {{\n\n}}\n```"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.8,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        echo=True
    )
    code = response.choices[0].text.strip()
    return code

# Generate and display the C++ code
if st.button("Generate Code"):
    if task:
        code = generate_code(task)
        st.code(code, language="cpp")
    else:
        st.warning("Please enter a programming task.")

    return generated_code
