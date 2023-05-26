import streamlit as st
import openai
import os
from configparser import ConfigParser

# Read API key from config file
config = ConfigParser()
config.read("config.ini")
api_key = config.get("openai", "api_key")

# Check if the API key is provided
if api_key is None or api_key == "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":
    st.error("OpenAI API key not found. Please provide your API key in the config.ini file.")
    st.stop()

# Set up OpenAI API credentials
openai.api_key = api_key

# Define the prompt for the OpenAI API
prompt = "Translate the following English text to French:"

# Streamlit app
def main():
    st.title("OpenAI Language Translation")
    text_input = st.text_area("Enter text to translate", value="Hello, how are you?")

    if st.button("Translate"):
        with st.spinner("Translating..."):
            # Call the OpenAI API to translate the text
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"{prompt}\n{text_input}\n-- Translation:",
                temperature=0.5,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )

            # Extract the translated text from the API response
            translation = response.choices[0].text.strip().split("-- Translation:")[1]

        st.success("Translation:")
        st.write(translation)

if __name__ == "__main__":
    main()
