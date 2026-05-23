import streamlit as st
import google.generativeai as genai

# API Setup
api_key = "AIzaSyD06pOGM-6kYj3uGYPzCOJDrcyX82unAtY"
genai.configure(api_key=api_key)

# If 'gemini-1.5-flash' is unavailable, try 'gemini-pro'
try:
    model = genai.GenerativeModel('gemini-flash-latest')
except Exception:
    model = genai.GenerativeModel('gemini-2.0-flash') 

st.title("Python AI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Generate Response
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    except Exception as e:
        # If an error still occurs, show which models are available
        st.error(f"Error: {e}")
        st.write("Checking available models for your API key...")
        models = [m.name for m in genai.list_models()]
        st.write(models)