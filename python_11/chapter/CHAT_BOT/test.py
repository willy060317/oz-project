import streamlit as st

with st.chat_message("user"):
    st.write("hello ")
prompt = st.chat_input("궁금한게 있으면 물어봐")