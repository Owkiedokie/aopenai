import streamlit as st
import openai

# Set up the OpenAI API
openai.api_key = st.secrets["api_key"]

def generate_code(task):
    # Prepare the prompt
    prompt = f"Task: {task}\n\n```cpp\n"
    
    # Generate the code using OpenAI's completions API
    response = openai.Completion.create(
        engine="text-davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
        prompt_model=None,
        log_level="info"
    )
    
    # Extract the generated code from the API response
    generated_code = response.choices[0].text
    
    return generated_code



def main():
    st.title("College Admission Chatbot")
    st.write("Welcome to the college admission chatbot! Please ask your questions below:")
    st.title("C++ Tutorial App")
    st.header("Generate Code for Basic Programming Tasks")
    
    # User input
    task = st.text_input("Enter the programming task:", "")
    
    if st.button("Generate Code"):
        # Call OpenAI API to generate code based on the task
        code = generate_code(task)
        
        # Display the generated code
        st.code(code)

def generate_code(task):
    # OpenAI code generation logic goes here
    # Use the task to generate the C++ code using OpenAI
    
    return generated_code

if __name__ == "__main__":
    main()
