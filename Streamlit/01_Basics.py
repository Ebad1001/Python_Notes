# A free and opensource framework to build and share (ML & DS) web apps

# !pip install streamlit
# !python -m streamlit run main.py


import streamlit as st

# Headings
st.title("This is a Title")  # Largest heading
st.header("This is a Header")  # Secondary heading
st.subheader("This is a Subheader")  # Tertiary heading
# Plain Texts
st.text("st.text: Some text")
st.write("st.write: Some text")
# Formatted Texts
st.markdown("st.markdown: **Bold text**, *italic text*, and click on the [link](https://www.google.com).")
st.latex(r"st.latex: a^2 + b^2 = c^2")
st.code("""
def hello_world():
    print("Hello, World!")
""", language="python")

# Expander
with st.expander("Expand for more details"):
    st.write("Here is some detailed information.")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")
else:
    st.write("Click the button to see something happen.")

# Text area
text = st.text_area("Enter a long message")
st.write(f"You wrote: {text}")

# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)
if age:
    st.write(f"You are {age} years old.")

# Slider
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {value}")

# Select slider
level = st.select_slider("Choose a level", options=["Low", "Medium", "High"], value="Medium")
st.write(f"You selected: {level}")

# Checkbox
check = st.checkbox("Show Text")
if check:
    st.write("You checked the box!")

# Radio
choice = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"You chose: {choice}")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# CheckGroup
selected = []
option1 = st.checkbox("Option 1")
if option1:
    selected.append("Option 1")
option2 = st.checkbox("Option 2")
if option2:
    selected.append("Option 2")
option3 = st.checkbox("Option 3")
if option3:
    selected.append("Option 3")
st.write(f"You selected: {selected}")

# Multiselect
options = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {options}")

# Date
date = st.date_input("Pick a date")
st.write(f"Selected date: {date}")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write("Uploaded file name:", uploaded_file.name)

# Color picker
color = st.color_picker("Pick a color", "#00f900")
st.write(f"The selected color is {color}")

# Progress bar
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)
st.write("Task completed!")

# Special Messages
st.success("This is a success message!")
st.error("This is an error message.")
st.warning("This is a warning.")
st.info("This is an informational message.")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("We are on Sidebar now!")


# publish your app on github
# add requirements.txt
# deploy on st community cloud
