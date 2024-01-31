import streamlit as st
from PIL import Image

st.title('This is a Chaney')

# Load the image
image = Image.open('./IMG_8849.JPG')

# Display the image
st.image(image)