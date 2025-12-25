from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Correct model name
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(user_text, image, prompt):
    response = model.generate_content(
        [user_text, image, prompt]
    )
    return response.text

st.set_page_config(
    page_title="Multilanguage Document Extractor",
    page_icon="🤖"
)
st.header("Multilanguage Document Extractor 🤖")

user_text = st.text_input("Enter your text here")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the document")

input_prompt = """
Extract the following information from the invoice image:
"""

if submit:
    if image is None:
        st.error("Please upload an image")
    else:
        response = get_gemini_response(
            user_text,
            image,
            input_prompt
        )
        st.subheader("Response")
        st.write(response)
