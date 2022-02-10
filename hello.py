import streamlit as st
from streamlit_chat import message

st.text_input('this')
message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
