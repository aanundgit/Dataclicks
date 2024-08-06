import streamlit as st
from datetime import date
from PIL import Image
import requests
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Product Demos",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title and Horizontal Line
st.markdown(
    """
    <style>
    .custom-title {
        color: #333;  /* Saffron yellow color */
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title with custom styling
st.markdown('<p class="custom-title">Product Demos </p>', unsafe_allow_html=True)
st.write("Current Date:", date.today())
st.markdown("""<hr style="height:2px;border:none;color:#F4C430;background-color:#3333" /> """,
            unsafe_allow_html=True)

# State to toggle expand/collapse
if 'expand_all' not in st.session_state:
    st.session_state.expand_all = False


def toggle_expand():
    st.session_state.expand_all = not st.session_state.expand_all


# Maximize/Collapse All Button
st.button("Maximize/Collapse All", on_click=toggle_expand)

# Widget URLs
widget_urls = [
    {"name":"Azure OpenAI Service Dream Demo for FSI","url":"https://regale.cloud/Microsoft/viewer/2723/azure-openai-service-dream-demo-for-fsi/index.html#/0/0"},
    {"name":"Microsoft Fabric with Azure Machine Learning Dream Demo TDM+BDM","url":"https://regale.cloud/Microsoft/viewer/2705/microsoft-fabric-with-azure-machine-learning-dream-demo/index.html#/0/0"},
    {"name":"PowerBI Differentiators Demo","url":"https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric end-to-end demo","url":"https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
    {"name":"Modern Analytics with Microsoft Fabric and Azure Databricks DREAM Lab","url":"https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
    {"name":"Modern Analytics with Azure Databricks and Power BI DREAM Demo (Partners)","url":"https://regale.cloud/Microsoft/viewer/2426/partners-modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name":"Modern Analytics with Azure Databricks and Power BI DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2421/modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name":"CosmosDB + OpenAI DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2493/cosmosdb-openai-dream-demo/index.html#/0/0"},
    {"name":"Azure OpenAI Service Dream demo with shopping co-pilot.","url":"https://regale.cloud/Microsoft/viewer/2486/azure-openai-service-dream-demo-with-shopping-co-pilot/index.html#/0/0"},
    {"name":"Azure OpenAI Service Dream Demo 10-minute","url":"https://regale.cloud/Microsoft/viewer/2383/azure-openai-service-dream-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric Dream Demo (10 minute)","url":"https://regale.cloud/Microsoft/viewer/2466/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric Dream Demo (5 minute)","url":"https://regale.cloud/Microsoft/viewer/2411/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric DREAM Demo (4 Minute) PARTNERS","url":"https://regale.cloud/Microsoft/viewer/2427/partners-microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric DREAM Demo (4 Minute)","url":"https://regale.cloud/Microsoft/viewer/2379/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name":"Azure OpenAI Service Dream Demo (with admin tool) 10-minute","url":"https://regale.cloud/Microsoft/viewer/2376/azure-openai-service-dream-demo-with-admin-tool/index.html#/0/0"},
    {"name":"Microsoft Fabric Embedded Demo","url":"https://regale.cloud/Microsoft/viewer/2262/microsoft-fabric-embedded-demo/index.html#/0/0"},
    {"name":"Microsoft Fabric and Azure Databricks DREAM Demo","url":"https://simdemo.azureedge.net/dai/fabric-databricks/index.html#/0/0"},
    {"name":"Microsoft Fabric and Azure Databricks DREAM Demo (Partners)","url":"https://regale.cloud/Microsoft/viewer/2428/partners-microsoft-fabric-and-azure-databricks-dream-demo/index.html#/0/0"},
    {"name":"Azure Databricks and Microsoft Fabric DREAM Demo (booth)","url":"https://regale.cloud/Microsoft/viewer/2303/azure-databricks-and-microsoft-fabric-dream-demo-booth/index.html#/0/0"},
    {"name":"Power BI Differentiators Dream Demo Full Click by Click","url":"https://regale.cloud/Microsoft/viewer/instance/2053/6338/index.html#/0/0"},
    {"name":"Analytics in MIDP Dream Demo for BDMs","url":"https://regale.cloud/Microsoft/viewer/2006/analytics-in-midp-dream-demo-for-bdms/index.html#/0/0"},
    {"name":"Power BI Differentiators Dream Demo Full Click by Click V2","url":"https://regale.cloud/Microsoft/viewer/1947/power-bi-differentiators-dream-demo-integrated-into-web-app/index.html#/0/0"}


]




# Columns
cols = st.columns(3)

# Custom JavaScript for modal functionality
st.markdown(
    """
    <script>
    function openModal(url) {
        var modal = document.getElementById("myModal");
        var iframe = document.getElementById("modalIframe");
        iframe.src = url;
        modal.style.display = "block";
    }

    function closeModal() {
        var modal = document.getElementById("myModal");
        var iframe = document.getElementById("modalIframe");
        iframe.src = "";
        modal.style.display = "none";
    }
    </script>
    """,
    unsafe_allow_html=True
)

# HTML for modal
st.markdown(
    """
    <div id="myModal" class="modal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.5);">
        <div class="modal-content" style="background-color: #fff; margin: 5% auto; padding: 20px; border: 1px solid #888; width: 90%; max-width: 900px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <span class="close" onclick="closeModal()" style="color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer;">&times;</span>
            <iframe id="modalIframe" src="" style="width: 100%; height: 70vh; border: none; border-radius: 8px;"></iframe>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Placeholder image URL
# Use a valid placeholder URL
placeholder_img_url = "https://via.placeholder.com/300"

# # Widget containers
# for i, widget in enumerate(widget_urls):
#     with cols[i % 3]:
#         # Display widget name as a clickable link that opens in a new window
#         st.markdown(f'''
#             <div style="text-align: center; margin-bottom: 10px;">
#                 <a href="{widget['url']}" target="_blank" style="text-decoration: none; color: #158237; font-weight: bold; font-size: 14px;">
#                     {widget['name']}
#                 </a>
#             </div>
#         ''', unsafe_allow_html=True)

#         # Expander with content
#         with st.expander("", expanded=st.session_state.expand_all):
#             try:
#                 st.markdown(f'''
#                     <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
#                         <iframe src="{widget['url']}" width="100%" height="100%" scrolling="yes" frameborder="0" allowfullscreen style="border: none; border-radius: 12px;"></iframe>
#                     </div>
#                 ''', unsafe_allow_html=True)
#             except:
#                 # Display placeholder image if iframe cannot be loaded
#                 st.markdown(f'''
#                     <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
#                         <img src="{placeholder_img_url}" alt="Preview Not Available" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
#                     </div>
#                 ''', unsafe_allow_html=True)

# new widget code


# Initialize session state attributes if they don't exist
if 'maximized_widget' not in st.session_state:
    st.session_state.maximized_widget = None
if 'expand_all' not in st.session_state:
    st.session_state.expand_all = False

# Function to handle maximizing an iframe


def toggle_maximize(widget_name):
    if st.session_state.maximized_widget == widget_name:
        st.session_state.maximized_widget = None
    else:
        st.session_state.maximized_widget = widget_name


# Columns layout
cols = st.columns(3)

# Placeholder image URL
placeholder_img_url = "https://via.placeholder.com/300"

# Custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    .overlay {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.8);
        transition: opacity 0.3s ease;
    }
    .overlay.active {
        display: block;
        opacity: 1;
    }
    .iframe-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        height: 90%;
        background-color: #fff;
        border: 1px solid #888;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        display: flex;
        flex-direction: column;
        padding: 10px;
        box-sizing: border-box;
    }
    .refresh-btn, .close-btn, .back-link {
        position: absolute;
        background: none;
        border: none;
        color: #007bff;
        cursor: pointer;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        transition: background 0.2s ease;
    }
    .refresh-btn {
        top: 10px;
        right: 10px;
        background: #007bff;
        color: white;
    }
    .refresh-btn:hover {
        background: #0056b3;
    }
    .close-btn {
        top: 10px;
        left: 10px;
        font-size: 28px;
        color: #aaa;
    }
    .close-btn:hover {
        color: black;
    }
    .back-link {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: #fff;
        color: #007bff;
        font-size: 18px;
        padding: 10px;
        border: 1px solid #007bff;
        border-radius: 5px;
        text-decoration: none;
        display: block;
    }
    .back-link:hover {
        background: #007bff;
        color: white;
    }
    @media only screen and (max-width: 768px) {
        .iframe-container {
            width: 100%;
            height: 100%;
            padding: 5px;
        }
        .refresh-btn, .close-btn, .back-link {
            font-size: 16px;
            padding: 8px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Widget containers
for i, widget in enumerate(widget_urls):
    with cols[i % 3]:
        # Display widget name as a clickable link that opens in a new window
        st.markdown(f'''
            <div style="text-align: center; margin-bottom: 10px;">
                <a href="{widget['url']}" target="_blank" style="text-decoration: none; color: #333; font-weight: bold; font-size: 14px;">
                    {widget['name']}
                </a>
            </div>
        ''', unsafe_allow_html=True)

        # Expander with content
        with st.expander("", expanded=st.session_state.expand_all):
            # Button to maximize the iframe
            st.button("Maximize", on_click=toggle_maximize, args=(
                widget['name'],), key=f"maximize-{widget['name']}")

            if st.session_state.maximized_widget == widget['name']:
                # Display the overlay for the maximized widget
                st.markdown(
                    f"""
                    <div class="overlay active">
                        <div class="iframe-container">
                            <button class="refresh-btn" onclick="window.location.reload();">Refresh the Browser to back to Home page</button>
                            <button class="close-btn" onclick="window.location.reload();">×</button>
                            <iframe src="{widget['url']}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
                            <a href="#" class="back-link" onclick="window.location.reload();"> </a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                try:
                    st.markdown(f'''
                        <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
                            <iframe src="{widget['url']}" width="100%" height="100%" scrolling="yes" frameborder="0" allowfullscreen style="border: none; border-radius: 12px;"></iframe>
                        </div>
                    ''', unsafe_allow_html=True)
                except:
                    # Display placeholder image if iframe cannot be loaded
                    st.markdown(f'''
                        <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
                            <img src="{placeholder_img_url}" alt="Preview Not Available" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                        </div>
                    ''', unsafe_allow_html=True)


# Custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1682685797857-97de838c192e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3387&q=80");
        background-size: cover;
        padding: 0 20px;
    }
    .sidebar .sidebar-content {
        background: url("");
    }
    .st-expander {
        margin-bottom: 20px;
        border: 1px solid #158237;
        border-radius: 12px;
        background-color: #fff;
    }
    .st-expander__header {
        display: none;
    }
    .st-expander__content {
        padding: 0;
    }
    a {
        text-decoration: none;
    }
    a:hover {
        color: #0d6a3b;
    }
    iframe {
        border-radius: 12px;
        padding: 0; /* Ensure no extra padding around iframe */
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
        margin: 5% auto; 
        padding: 20px; 
        border: 1px solid #888; 
        width: 90%; 
        max-width: 900px; 
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
    @media only screen and (max-width: 768px) {
        iframe {
            height: calc(100vw / 1.5) !important;
        }
        .st-expander {
            width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True



)
