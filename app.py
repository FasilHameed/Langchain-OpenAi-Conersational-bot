import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="Conversational Q&A Chatbot",
    page_icon=":robot_face:",
    layout="centered"
)

# Custom CSS for beautification
st.markdown("""
<style>
body {
    color: #333;
    background-color: #f0f2f6;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
.stTextInput > div > div > input {
    border-radius: 15px;
    border: 1px solid #ccc;
    padding: 10px 15px;
    font-size: 16px;
}
.stButton > button {
    border-radius: 15px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}
.stButton > button:hover {
    background-color: #45a049;
}
.stHeader {
    color: #4CAF50;
    font-size: 32px;
    text-align: center;
    margin-bottom: 30px;
}
.stSubheader {
    color: #333;
    font-size: 24px;
    text-align: center;
    margin-bottom: 20px;
}
.stSidebar {
    background-color: #fff;
    padding: 20px;
    border-radius: 15px;
}
.stFooter {
    color: #666;
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}
.stBotMessage {
    font-style: italic;
    color: #666;
}
.stInfo {
    color: #4287f5;
    font-size: 16px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Conversational Chat Bot 🤖")
st.markdown("---")

chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are an intelligent bot.")
    ]


def get_chat_model_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


input_text = st.text_input('Ask a question:', key="input")
response = get_chat_model_response(input_text)

submit_button = st.button("Ask the question")

if submit_button:
    st.subheader("The Response is:")
    st.write(response)

# Footer
st.markdown("---")
st.markdown("Powered by OpenAI")
st.markdown("*Made with ❤️ by Fasil Hameed*")