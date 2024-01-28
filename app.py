import streamlit as st
import time
from prompt import firePrompt

st.set_page_config(page_title='Tamil LLM',
                   page_icon='💁🏻‍♂️',
                   layout='wide',
                   initial_sidebar_state='expanded'
                )

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'temp' not in st.session_state:
    st.session_state.temp = 0

with st.sidebar:
    st.markdown('## எனது கற்பனை திறனை தேர்வு செய்க !', unsafe_allow_html=True)
    st.session_state.temp = st.slider(label='temp', min_value=0.0, 
                                      max_value=1.0, step=0.1, value=0.3, label_visibility='hidden')
    st.image('sidebar_logo.png', use_column_width=True)
    st.image('cit_logo_small.png', use_column_width=True)

def getAvatar(role):
    if role == 'assistant':
        return "tamil-llama-logo2.png"
    else :
        return "cit_logo_small.png"

def getContext():
    res = ""
    for item in st.session_state.messages[:-1]:
        res = res + f"role : {item['role']} content : {item['content']}\n"
    return res

st.markdown('# :rainbow[Local] 🏠 :rainbow[Private] 🔒 :rainbow[தமிழ் AI Assistant] 🤖', unsafe_allow_html=True)
st.markdown('## :rainbow[Powered by தமிழ் 🦙🦙🦙 ] ', unsafe_allow_html=True)

with st.chat_message(name="assistant", avatar='tamil-llama-logo2.png'):
    st.markdown('#### Ask me anything! என்னிடம் தமிழிலும் உரையாடலாம்! 🙏🏻')
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=getAvatar(message["role"])):
        st.markdown(f'{message["content"]}')

if prompt := st.chat_input(placeholder="Chat with me. என்னிடம் தமிழிலும் உரையாடலாம்!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar='cit_logo_small.png'):
        st.markdown(prompt)
    with st.chat_message(name='assistant', avatar='tamil-llama-logo2.png'):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner(text="Thinking... 💭💭💭"):
            raw = firePrompt(st.session_state.messages[-1]['content'], temp=st.session_state.temp)
            response = str(raw)
            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
            message_placeholder.markdown(f'#### {full_response}', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
