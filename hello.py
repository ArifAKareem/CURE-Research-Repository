import streamlit as st
from streamlit_chat import message

msg = st.text_input('this')

while true: 
  message("My message") 
  message(msg, is_user=True)  # align's the message to the right
