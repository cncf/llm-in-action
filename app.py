import os
import streamlit as st
from ollama import Client

ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

def process_stream(stream):
  for chunk in stream:
   yield chunk['message']['content']

# Streamlit UI

styl = f"""
<style>
    /* not great support for :has yet (hello FireFox), but using it for now */
    .main {{
        background-image: url('https://vior-lys.s3.amazonaws.com/img/kccneu24.png'); 
        background-repeat: repeat;
        background-size: cover;
        background-attachment: fixed;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

st.title('Describe an Image with LLaVa 📸')
picture = st.camera_input("Take a picture. Say Kubernetes!")

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