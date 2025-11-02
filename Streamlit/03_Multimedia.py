# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
from PIL import Image


# Images

# Load image from URL
st.header("Image from URL")
img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_1NAkAlloA8yWNqiGzh8iZa8xwx_gri_Tgg&s"
st.image(img_url, caption="Image from URL")
# Load image from file
st.header("Image from file")
img = Image.open(".//assets//image.png")
st.image(img, caption="My Uploaded Image")


# Audios

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)
# Load audio from file
st.header("Audio from file")
audio_file = open(".//assets//audio.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mpeg")


# Videos

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
st.video(video_url)
# Load video from file
st.header("Video from file")
video_file = open(".//assets//video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
