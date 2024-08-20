import streamlit as st
from datetime import date

# Page Configuration
st.set_page_config(
    page_title="Architecture Diagrams",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title and Horizontal Line

st.markdown(
    """
    <style>
    .custom-title {
        color: #324ab2;  /* Violet */
        font-size: 40px;
        font-weight: bold;
    }
    .carousel-container {
        position: relative;
        width: 100%;
        max-width: 1100px;  /* Smaller max-width for smaller images */
        margin: 0 auto;  /* Center the container */
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        background: #f0f0f0;
        border: 10px solid #f0f0f0;
    }
    .carousel-image {
        width: 100%;
        height: auto;  /* Adjust height automatically */
        object-fit: contain;  /* Ensure the image fits within the container while maintaining aspect ratio */
        border-radius: 15px;  /* Round the corners of the image */
    }
    .arrow-left, .arrow-right {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        border-radius: 50%;
        font-size: 24px;
        z-index: 1;
        transition: background-color 0.3s;
    }
    .arrow-left {
        left: 10px;
    }
    .arrow-right {
        right: 10px;
    }
    .arrow-left:hover, .arrow-right:hover {
        background-color: rgba(0, 0, 0, 0.8);
    }
    .image-name {
        text-align: center;
        font-weight: bold;
        padding: 10px;
        font-size: 24px;  /* Large font size for better readability */
        color: #324ab2;  /* Matching title color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<p class="custom-title">Architecture Diagrams </p>', unsafe_allow_html=True)
st.write("Current Date:", date.today()) 
st.markdown("""<hr style="height:2px;border:none;color:#324ab2;background-color:#324ab2;" /> """,
            unsafe_allow_html=True)

images = [
    {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/daidemo_fabric_3_demo_arch_V2.gif", "name": "Fabric Demo Architecture 3.0"},
    {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/fabric_2_demo_arch.gif", "name": "Fabric Demo Architecture 2.0"},
    {"url": "https://dreamdemoassets.blob.core.windows.net/snowflake/snowflake_demo_architecture.png", "name": "Snowflake Demo Architecture"},
    {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/Fabric_ADB_Architecture_Diagram.gif", "name": "Fabric Azure Databricks Architecture "},
    {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/purview_demo_arch_4.png", "name": "Purview Demo Architecture"},
    {"url": "https://nrfcdn.azureedge.net/fab_db_2_arch_diagram.gif", "name": "Microsoft Fabric Databricks 2.0 Architecture"},
    {"url": "https://dreamdemoassets.blob.core.windows.net/manufacturing/Mfg_with_fabric_arch_1.gif", "name": "Manufacturing with Fabric Architecture"},
    {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/Fabric_AML_Arc.png", "name": "Fabric Azure AML Architecture"},
    {"url": "https://nrfcdn.azureedge.net/mfdb2_onelake_architecture.png", "name": "Microsoft Fabric Databricks 2.0 Onelake Architecture"},
    {"url": "https://nrfcdn.azureedge.net/mfigdb_onelake_architecture.gif", "name": "Microsoft Fabric Databricks Onelake Architecture"},
]

# Initialize the session state for image index
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to display the carousel with the current image and name
def display_carousel():
    image_url = images[st.session_state.current_index]['url']
    image_name = images[st.session_state.current_index]['name']
    st.markdown(
        f"""
        <div class="carousel-container">
            <img class="carousel-image" src="{image_url}" alt="Carousel Image"/>
           
        </div>
        <div class="image-name">{image_name}</div>
        """,
        unsafe_allow_html=True
    )

# Display the carousel
display_carousel()

# Add Streamlit buttons for navigation
col1, col2 = st.columns([1, 8])
with col1:
    if st.button("◀", key="prev"):
        st.session_state.current_index = (st.session_state.current_index - 1) % len(images)
      
with col2:
    if st.button("▶", key="next"):
        st.session_state.current_index = (st.session_state.current_index + 1) % len(images)
       
# Optional content below the carousel
st.markdown("Navigate through the Architecture Diagrams using the arrows.")