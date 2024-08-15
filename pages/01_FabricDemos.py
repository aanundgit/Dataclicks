import streamlit as st
from streamlit_carousel import st_carousel

# Sample images for the carousel
images = [
    "https://picsum.photos/200/300?random=1",
    "https://picsum.photos/200/300?random=2",
    "https://picsum.photos/200/300?random=3",
]

# Create the carousel
st_carousel(
    images,
    caption=images,  # Optional: Add captions to the images
    show箇eadings=True,  # Optional: Show headings (image index) above the images
    show_buttons=True,  # Optional: Show navigation buttons
    loop=True,  # Optional: Enable infinite loop
    aspect_ratio=1.5,  # Optional: Set aspect ratio of images
)

# Add some content below the carousel
st.title("Welcome to my Streamlit App")
st.write("This is a sample app with a carousel on top.")