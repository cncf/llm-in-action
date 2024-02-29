import os
import streamlit as st
from PIL import Image
import requests
from langchain_community.llms import Ollama

ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Placeholder for your Ollama LLaVa model interfacing function
def describe_picture(image):
    llm = Ollama(model="llava", base_url=ollama_base_url)

    # Placeholder return statement
    return "This is where the image description will appear."

# Streamlit UI
st.title('Image Description with LLaVa')

img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    st.image(image, caption='Uploaded Image:', use_column_width=True)
    st.write("")
    st.write("Describing...")
    #description = describe_picture(img_file_buffer)
    #st.write(description)
