import streamlit as st
import openai

# Set up the OpenAI API
openai.api_key = st.secrets["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"]

# Title of the app
st.title("C++ Code Generator")

# User input for the programming task
task = st.text_input("Enter the programming task:")

# Generate C++ code using OpenAI's GPT-3.5 model
def generate_code(prompt):
    model_engine = "text-davinci-002"  # Select the OpenAI GPT-3 model to use
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    code = response.choices[0].text.strip()
    return code

def main():
    st.set_page_config(page_title="C++ Tutorial App")
    st.title("C++ Tutorial App")
    task = st.selectbox("Select a programming task:", [
        "Hello World",
        "Sum of Two Numbers",
        "Factorial",
        "Fibonacci Sequence",
    ])
    if task == "Hello World":
        prompt = "Write a C++ program that prints 'Hello, world!' to the console."
    elif task == "Sum of Two Numbers":
        prompt = "Write a C++ program that asks the user for two numbers and prints their sum."
    elif task == "Factorial":
        prompt = "Write a C++ program that asks the user for a number and prints its factorial."
    else:  # task == "Fibonacci Sequence"
        prompt = "Write a C++ program that asks the user for a number n and prints the first n numbers of the Fibonacci sequence."
    code = generate_code(prompt)
    st.code(code, language="cpp")

if __name__ == "__main__":
    main()
