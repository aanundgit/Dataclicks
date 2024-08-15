import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Professional business images for the carousel
images = [
    "https://picsum.photos/900/200?random=1",
    "https://picsum.photos/800/400?random=2",
    "https://picsum.photos/800/400?random=3",
]



# Initialize session state for theme and current image index
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to toggle the theme
def toggle_theme():
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

# Toggle button for theme change
if st.button(f'Switch to {"Dark" if st.session_state.theme == "light" else "Light"} Theme'):
    toggle_theme()

# Apply theme styles
if st.session_state.theme == 'dark':
    st.markdown(
        """
        <style>
        body {
            background-color: #333;
            color: #fff;
        }
        .arrow-button {
            background-color: #555;
            color: #fff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #fff;
            color: #000;
        }
        .arrow-button {
            background-color: #007BFF;
            color: #fff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display the current image
def display_image(index):
    response = requests.get(images[index])
    img = Image.open(BytesIO(response.content))
    st.image(img, use_column_width=True)  # Ensure image fills the column width

# Custom CSS to make the image fill the width of the page
st.markdown(
    """
    <style>
    .stImage > div {
        display: flex;
        justify-content: center;
    }
    img {
        width: 100% !important;
        height: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the current image
display_image(st.session_state.current_index)

# Custom CSS for navigation arrows
st.markdown("""
    <style>
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .arrow-button {
        border: none;
        padding: 10px 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation arrows with responsive design
col1, col2, col3 = st.columns([1, 8, 1])
with col1:
    if st.button("<", key="prev", help="Previous Image", on_click=lambda: setattr(st.session_state, 'current_index', (st.session_state.current_index - 1) % len(images))):
        display_image(st.session_state.current_index)
with col2:
    st.write("")  # Spacer to center the image
with col3:
    if st.button(">", key="next", help="Next Image", on_click=lambda: setattr(st.session_state, 'current_index', (st.session_state.current_index + 1) % len(images))):
        display_image(st.session_state.current_index)

# Add some content below the carousel
st.markdown("<h1 style='text-align: center;'>Welcome to my Streamlit App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>This is a sample app with an image carousel on top.</p>", unsafe_allow_html=True)
