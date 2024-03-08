import os
import base64
import streamlit as st
from ollama import Client

ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

def process_stream(stream):
  for chunk in stream:
   yield chunk['message']['content']

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Streamlit UI

base64_image = get_base64_encoded_image('img/kccneu24.png')
styl = f"""
<style>
    .main {{
        background-image: url(data:image/png;base64,{base64_image}); 
        background-repeat: repeat;
        background-size: cover;
        background-attachment: fixed;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

st.title(':grey[Describe an Image with LLaVa 📸]')
picture = st.camera_input("")

st.subheader(':grey[Take a picture. Say ] :blue[_Kubernetes_]:grey[!]')

if picture:
  with open ('snap.jpg','wb') as f:
    f.write(picture.getbuffer())

  # Initialize the Ollama client
  client = Client(host=ollama_base_url)

  # Define the path to your image
  image_path = 'snap.jpg'

  # Prepare the message to send to the LLaVA model
  message = {
      'role': 'user',
      'content': 'Describe this image in a respectful way, without mentioning any text elements.',
      'images': [image_path]
  }

  # Use the ollama.chat function to send the image and retrieve the description
  stream = client.chat(
      model="llava",  # Specify the desired LLaVA model size
      messages=[message],
      stream=True,
  )
  
  st.write_stream(process_stream(stream))