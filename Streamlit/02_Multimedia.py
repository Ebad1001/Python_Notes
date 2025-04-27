# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
from PIL import Image

### IMAGES ###

# Load image from URL
st.header("Image from URL")
img_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-lighttext.png"
st.image(img_url, caption="Image from URL")

# Load image from file
st.header("Image from file")
img = Image.open(".//assets//image.png")
st.image(img, caption="My Uploaded Image")

### AUDIOS ###

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)

# Load audio from file
st.header("Audio from file")
audio_file = open(".//assets//audio.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mpeg")

### VIDEOS ###

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
if st.button("Click to play video"):
    st.video(video_url)

# Load video from file
st.header("Video from file")
video_file = open(".//assets//video2.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)