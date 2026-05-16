import streamlit as st
from chatbot import ask_bot
import base64

# Load background image
with open("shiv.jpg", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

# CSS styling
css = f"""
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.main .block-container {{
    max-width: 850px;
    margin-top: 40px;
    padding: 2.5rem;
    border-radius: 25px;
    background: rgba(15, 23, 42, 0.45);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
}}

h1 {{
    text-align: center;
    color: #FFD700 !important;
    text-shadow: 0 0 12px rgba(0,0,0,0.8);
}}

p, label, div {{
    color: white !important;
}}

.stTextInput input {{
    background: rgba(255, 255, 255, 0.92);
    color: black !important;
    border-radius: 12px;
    font-size: 18px;
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Title
st.title("🕉️ Amarnath Yatra AI Bot")

st.markdown(
    "<h3 style='text-align:center; color:#FFD700;'>ॐ नमः शिवाय</h3>",
    unsafe_allow_html=True,
)

# Input
question = st.text_input("Ask your question:")

# Response
if question:
    with st.spinner("🔱 Seeking Lord Shiva's wisdom..."):
        answer = ask_bot(question)
    st.write(answer)