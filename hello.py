import streamlit as st
from streamlit_chat import message

msg = st.text_input('this')


while True: 
  message("My message", "this") 
  message(msg, is_user=True)  # align's the message to the right
  
