import streamlit as st
from datetime import date
from PIL import Image
import requests
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Microsoft Fabric Demos",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title and Horizontal Line
st.title(":green[Microsoft Fabric Demos]")
st.write("Current Date:", date.today())
st.markdown("""<hr style="height:2px;border:none;color:#158237;background-color:#158237;" /> """, unsafe_allow_html=True)

# State to toggle expand/collapse
if 'expand_all' not in st.session_state:
    st.session_state.expand_all = False
if 'search_query' not in st.session_state:
    st.session_state.search_query = ''

def toggle_expand():
    st.session_state.expand_all = not st.session_state.expand_all

def update_search_query():
    st.session_state.search_query = st.session_state.search_input

# Search Box
st.text_input("Search Widgets", key='search_input', on_change=update_search_query)

# Maximize/Collapse All Button
st.button("Maximize/Collapse All", on_click=toggle_expand)

# Widget URLs
widget_urls = [
    {"name": "Fabric-Guided Tour", "url": "https://guidedtour.microsoft.com/en-us/guidedtour/microsoft-fabric/microsoft-fabric/1/1"},
    {"name": "Fabric Blog", "url": "https://partner.microsoft.com/en-us/asset/collection/industry-dream-demos-and-dream-demo-in-a-box#/"},
    {"name": "Fabric Full Demo", "url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
    # Add more widgets as needed...
]

# Filter widgets based on search query
filtered_widget_urls = [widget for widget in widget_urls if st.session_state.search_query.lower() in widget['name'].lower()]

# Columns layout
cols = st.columns(2)

# Placeholder image URL
placeholder_img_url = "https://via.placeholder.com/300"

# Custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    .iframe-container {
        position: relative;
        width: 100%;
        height: 300px;
        padding: 5px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    .iframe-container iframe {
        width: 100%;
        height: 100%;
        border: none;
        border-radius: 12px;
    }
    .modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.5);
    }
    .modal-content {
        background-color: #fff;
        margin: 2% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 95%;
        max-width: 1200px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }
    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to handle maximizing an iframe
def toggle_maximize(widget_name):
    if st.session_state.maximized_widget == widget_name:
        st.session_state.maximized_widget = None
    else:
        st.session_state.maximized_widget = widget_name

# Initialize session state attributes if they don't exist
if 'maximized_widget' not in st.session_state:
    st.session_state.maximized_widget = None

# Function to render the iframe or placeholder image
def render_iframe_or_image(url, height='300px'):
    try:
        st.markdown(f'''
            <div class="iframe-container" style="height: {height};">
                <iframe src="{url}" frameborder="0" allowfullscreen></iframe>
            </div>
        ''', unsafe_allow_html=True)
    except:
        st.image(placeholder_img_url, caption="Preview Not Available")

# Iterate over filtered widgets and display them
current_col = 0
for i, widget in enumerate(filtered_widget_urls):
    with cols[current_col].expander(widget['name'], expanded=st.session_state.expand_all):
        st.button("Maximize", on_click=toggle_maximize, args=(widget['name'],), key=f"maximize-{widget['name']}")

        if st.session_state.maximized_widget == widget['name']:
            # Display the modal for the maximized widget
            st.markdown(
                f"""
                <div class="modal" style="display:block;">
                    <div class="modal-content">
                        <span class="close" onclick="window.location.reload();">&times;</span>
                        <iframe src="{widget['url']}" width="100%" height="700px" frameborder="0" allowfullscreen></iframe>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            render_iframe_or_image(widget['url'])

    # Toggle column for next widget
    current_col = (current_col + 1) % 2
