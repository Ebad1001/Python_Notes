# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
import random as rn

# Sidebar
st.sidebar.title("Sidebar Title")
choice = st.sidebar.radio("Select a view:", ["Home", "About", "Contact"])

st.header("Sidebar")
st.write(f"This is the {choice} page!")

# Columns
st.header("Columns")
col1, col2 = st.columns([1, 2])  # col2 is twice as wide as col1
with col1:
    st.write("This is the first column")
    st.write("We can use it as the input section")
    passwordSize = st.slider("Pick Password Size", 4, 20)
with col2:
    st.write("This is the second column")
    st.write("We can use it as the output section")
    password = ""
    for i in range(passwordSize):
        x = rn.randint(0, 25)
        password += chr(ord('A') + x)
    st.write(f"You password: {password}")


# Tabs
st.header("Tabs")
tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Info"])
with tab1:
    st.write("Chart view")
with tab2:
    st.write("Data view")
with tab3:
    st.write("Information view")

# Container: There are 2 ways to work with containers
st.header("Containers")

# 1st way: Assigning container to a variable
cont= st.container()
st.write("This is outside the container")
cont.line_chart([1, 2, 3])
st.write("This is outside the container")

# 2nd way: Using with context block
with st.container():
    st.write("Hello Hello Hello")
    st.button("I am a Button")
