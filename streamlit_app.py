import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.chat_message("ai").write("hi")
st.chat_message("human").write("hi")
st.write("asd")

with st.sidebar:
    "1. asd"
    "2. sdf"