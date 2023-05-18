import streamlit as st
import openai

# Set up the OpenAI API
openai.api_key = st.secrets["api_key"]

qa_pairs = {
    "What are the hours of operation?": "The college is generally open from 9:00 AM to 5:00 PM, but some departments may have different hours.",
    "What is the dress code for students?": "We do not have a strict dress code, but we encourage students to dress appropriately for classes and other college events.",
    "What is the college's mission statement?": "Our mission is to provide a comprehensive education that prepares students for successful careers and responsible citizenship.",
    "What is the college culture like?": "Our college culture is inclusive, collaborative, and supportive. We value diversity and strive to create a welcoming environment for all students.",
    "What kind of benefits do students receive?": "Our college offers a wide range of benefits to students, including access to health services, career counseling, and financial aid programs. We also provide opportunities for students to participate in extracurricular activities and leadership programs.",
}

def generate_response(question):
    if question in qa_pairs:
        return qa_pairs[question]
    else:
        prompt = f"Q: {question}\nA:"
        try:
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()
            return response
        except openai.error.RateLimitError as e:
            return "API rate limit exceeded. Please try again later."
        except Exception as e:
            return "An error occurred. Please try again."


def main():
    st.title("College Admission Chatbot")
    st.write("Welcome to the college admission chatbot! Please ask your questions below:")

    counter = 0  # Initialize a counter

    while True:
        try:
            question = st.text_input("> ", key=f"user_input_{counter}")  # Assign a unique key to each text_input widget
            if question.lower() == "quit":
                break
            else:
                response = generate_response(question)
                st.write(response)
            counter += 1  # Increment the counter
        except KeyboardInterrupt:
            st.write("Program interrupted. Exiting...")
            break


if __name__ == "__main__":
    main()
