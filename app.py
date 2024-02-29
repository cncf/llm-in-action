import os
import streamlit as st
from ollama import Client

ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

# Streamlit UI
st.title('Image Description with LLaVa 📸')
picture = st.camera_input("Take a picture")

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
  response = client.chat(
      model="llava",  # Specify the desired LLaVA model size
      messages=[message],
  )
  st.write(response['message']['content'])