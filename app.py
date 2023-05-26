import streamlit as st
import openai
import requests
import os
import tempfile
import gdown

# Load API key from file on Google Drive
file_url = 'https://drive.google.com/uc?id=12mWdxLePVnbeemH4AozHia6Rx_5crpay'  # Replace with your file URL
temp_file_path = tempfile.mktemp()
gdown.download(file_url, temp_file_path)
with open(temp_file_path, 'r') as f:
    api_key = f.read().strip()

if not api_key:
    st.error("OpenAI API key not found. Please provide your API key.")
    st.stop()

# Define the API endpoint
endpoint = "https://api.openai.com/v1/engines/davinci/completions"

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
            try:
                # Prepare the headers and payload
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                }
                payload = {
                    "prompt": f"{prompt}\n{text_input}\n-- Translation:",
                    "temperature": 0.5,
                    "max_tokens": 100,
                    "top_p": 1.0,
                    "frequency_penalty": 0.0,
                    "presence_penalty": 0.0,
                }

                # Send the POST request to the OpenAI API
                response = requests.post(endpoint, headers=headers, json=payload)

                # Print the response JSON for debugging
                st.write(response.json())

                # Extract the translated text from the API response
                data = response.json()
                choices = data["choices"]
                if len(choices) > 0:
                    translation = choices[0]["text"].strip()
                    st.success("Translation:")
                    st.write(translation)
                else:
                    st.error("No translation found.")

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred during the API request: {str(e)}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
