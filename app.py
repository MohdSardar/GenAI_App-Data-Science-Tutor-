import google.generativeai as genai
import streamlit as st

# Read the API key and setup a Gemini client
f = open(".gemini.txt")
key = f.read()

genai.configure(api_key=key)

st.markdown("<h1 style='color:Blue;'>GenAI-App : Data Science Tutor</h1>", unsafe_allow_html=True)


# Take user's input
prompt = st.text_area("Ask me anything about data science", height=100)

# If button is clicked, generate responses
if st.button("Ask"):
    # st.markdown("<h2 style='color:black;'>Review:</h2>", unsafe_allow_html=True)

    # Original Code
    # st.markdown("<h3 style='color:green;font-size:20px;'>Original Code:</h3>", unsafe_allow_html=True)
    # st.code(prompt, language='python')

    model = genai.GenerativeModel('gemini-pro')

    chat = model.start_chat(history=[])

    response = chat.send_message(prompt)



    # Display corrected code
    output = response.text
    # st.markdown("<h3 style='color:green;font-size:20px;'>Corrected Code and review:</h3>", unsafe_allow_html=True)
    st.write(output)
