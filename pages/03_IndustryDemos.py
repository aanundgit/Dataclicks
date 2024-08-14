import streamlit as st
from datetime import date
from PIL import Image
import requests
from io import BytesIO
# import hmac

# #--- authenticate with password ---

# def check_password():
#     """Returns `True` if the user had the correct password."""

#     def password_entered():
#         """Checks whether a password entered by the user is correct."""
#         if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]  # Don't store the password.
#         else:
#             st.session_state["password_correct"] = False

#     # Return True if the password is validated.
#     if st.session_state.get("password_correct", False):
#         return True

#     # Show input for password.
#     st.text_input(
#         "Password", type="password", on_change=password_entered, key="password"
#     )
#     if "password_correct" in st.session_state:
#         st.error("😕 Password incorrect")
#     return False


# if not check_password():
#     st.stop()  # Do not continue if check_password is not True.

# # Main Streamlit app starts here
# st.write("Here goes your normal Streamlit app...")
# st.button("Click me")




















# Page Configuration
st.set_page_config(
    page_title="Microsoft Fabric Demos",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title and Horizontal Line
st.title(":blue[Industry Demos]")
st.write("Current Date:", date.today())
st.markdown("""<hr style="height:2px;border:none;color:#317ae8;background-color:#317ae8;" /> """, unsafe_allow_html=True)

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
    {"name":"Retail Industry -Customer Insights demo","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
    #{"name":"Fabric Demo","url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
    {"name": "Retail Industry Demo", "url": "https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Retail%20Industry%20Scenario%20DREAM%20Demo"},
    {"name":"Finance Industry Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Financial%20Services%20Industry%20DREAM%20Demo"},
    {"name":"Manufacturing Industry Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Manufacturing%20Industry%20Scenario%20DREAM%20Demo"},
    {"name":"Healthcare Industry - BDM Demo","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"},
    {"name":"Healthcare Industry - TDM Demo","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
    #{"name":"Healthcare Industry - V1","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Healthcare%20Industry%20Scenario%20DREAM%20Demo"},
    {"name":"Sustainability Demo","url":"https://app-sustainabilitydemo-prod.azurewebsites.net/#/login"},
    {"name":"Public Finance Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
    {"name":"Public Finance Full Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
    {"name":"Consumer Goods DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2249/consumer-goods-dream-demo/index.html#/0/0"},
    {"name":"Healthcare DREAM demo for TDM","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
    {"name":"Customer Insights demo for Retail Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
    {"name":"Customer Insights demo for Financial Services Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2218/customer-insights-for-financial-services-industry-dream-demo/index.html#/0/0"},
    {"name":"Healthcare Industry Scenario Dream Demo","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"}
   
   
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
                        <iframe src="{widget['url']}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            render_iframe_or_image(widget['url'])

    # Toggle column for next widget
    current_col = (current_col + 1) % 2















#-- code with out search filter ------------------------
# import streamlit as st
# from datetime import date
# from PIL import Image
# import requests
# from io import BytesIO

# # Page Configuration
# st.set_page_config(
#     page_title="Microsoft Fabric Demos",
#     page_icon="",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Title and Horizontal Line
# st.title(":blue[Industry Demos]")
# st.write("Current Date:", date.today())
# st.markdown("""<hr style="height:2px;border:none;color:#317ae8;background-color:#317ae8;" /> """,
#             unsafe_allow_html=True)

# # State to toggle expand/collapse
# if 'expand_all' not in st.session_state:
#     st.session_state.expand_all = False

# def toggle_expand():
#     st.session_state.expand_all = not st.session_state.expand_all

# # Maximize/Collapse All Button
# st.button("Maximize/Collapse All", on_click=toggle_expand)

# # Widget URLs
# widget_urls = [
# {"name":"Dynamics-CustomerInsights","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
#     {"name":"Fabric","url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
#     {"name": "Retail Industry", "url": "https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Retail%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Finance Industry","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Financial%20Services%20Industry%20DREAM%20Demo"},
#     {"name":"Manufacturing Industry","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Manufacturing%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Healthcare Industry - BDM","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"},
#     {"name":"Healthcare Industry - TDM","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
#     {"name":"Healthcare Industry - V1","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Healthcare%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Sustainability","url":"https://app-sustainabilitydemo-prod.azurewebsites.net/#/login"},
#     {"name":"Public Finance","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
#     {"name":"Public Finance Full Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
   
#     {"name":"Consumer Goods DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2249/consumer-goods-dream-demo/index.html#/0/0"},
#     {"name":"Healthcare DREAM demo for TDM","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
#     {"name":"Customer Insights for Retail Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
#     {"name":"Customer Insights for Financial Services Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2218/customer-insights-for-financial-services-industry-dream-demo/index.html#/0/0"},
#     {"name":"Healthcare Industry Scenario Dream Demo","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"}
   
   
# ]

# # Placeholder image URL
# placeholder_img_url = "https://via.placeholder.com/300"

# # Initialize session state attributes if they don't exist
# if 'maximized_widget' not in st.session_state:
#     st.session_state.maximized_widget = None

# # Function to handle maximizing an iframe
# def toggle_maximize(widget_name):
#     if st.session_state.maximized_widget == widget_name:
#         st.session_state.maximized_widget = None
#     else:
#         st.session_state.maximized_widget = widget_name

# # Custom CSS for styling and responsiveness
# st.markdown(
#     """
#     <style>
#     body {
#         font-family: Arial, sans-serif;
#         background-color: #f5f5f5;
#     }
#     .stButton button {
#         width: 100%;
#         background-color: #317ae8;
#         color: white;
#         border: none;
#         border-radius: 5px;
#         padding: 10px;
#         cursor: pointer;
#         transition: background-color 0.3s;
#     }
#     .stButton button:hover {
#         background-color: #0d6a3b;
#     }
#     .st-expander {
#         border: 1px solid #317ae8;
#         border-radius: 12px;
#         background-color: #ffffff;
#         margin-bottom: 20px;
#     }
#     .st-expander__header {
#         font-size: 1.1em;
#         font-weight: bold;
#         color: #317ae8;
#         padding: 10px 0;
#         text-align: center;
#     }
#     .st-expander__content {
#         padding: 0 10px 10px 10px;
#     }
#     .iframe-container {
#         position: relative;
#         width: 100%;
#         padding-top: 56.25%;
#         margin-bottom: 10px;
#     }
#     .iframe-container iframe {
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         border: none;
#         border-radius: 12px;
#     }
#     .modal {
#         display: none; 
#         position: fixed; 
#         z-index: 1000; 
#         left: 0; 
#         top: 0; 
#         width: 100%; 
#         height: 100%; 
#         overflow: auto; 
#         background-color: rgba(0,0,0,0.5); 
#     }
#     .modal-content {
#         background-color: #fff; 
#         margin: 5% auto; 
#         padding: 20px; 
#         border: 1px solid #888; 
#         width: 90%; 
#         max-width: 900px; 
#         border-radius: 12px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
#     .close {
#         color: #aaa;
#         float: right;
#         font-size: 28px;
#         font-weight: bold;
#     }
#     .close:hover,
#     .close:focus {
#         color: black;
#         text-decoration: none;
#         cursor: pointer;
#     }
#     @media (max-width: 768px) {
#         .modal-content {
#             width: 95%;
#         }
#         .iframe-container {
#             padding-top: 75%;
#         }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Placeholder function to render iframes or images
# def render_iframe_or_image(url, height='300px'):
#     try:
#         st.markdown(f'''
#             <div class="iframe-container" style="height: {height};">
#                 <iframe src="{url}" frameborder="0" allowfullscreen></iframe>
#             </div>
#         ''', unsafe_allow_html=True)
#     except:
#         st.image(placeholder_img_url, caption="Preview Not Available")

# Two-column layout for widget containers
# col1, col2 = st.columns(2)
# columns = [col1, col2]
# current_col = 0

# for i, widget in enumerate(widget_urls):
#     with columns[current_col].expander(widget['name'], expanded=st.session_state.expand_all):
#         st.button("Maximize", on_click=toggle_maximize, args=(widget['name'],), key=f"maximize-{widget['name']}")

#         if st.session_state.maximized_widget == widget['name']:
#             # Display the modal for the maximized widget
#             st.markdown(
#                 f"""
#                 <div class="modal" style="display:block;">
#                     <div class="modal-content" style="width: 95%; max-width: 1200px;">
#                         <span class="close" onclick="window.location.reload();">&times;</span>
#                         <iframe src="{widget['url']}" width="100%" height="700px" frameborder="0" allowfullscreen></iframe>
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#         else:
#             render_iframe_or_image(widget['url'])

#     # Toggle column for next widget
#     current_col = (current_col + 1) % 2
















#---------------------------------- old code three column format ------------------
# import streamlit as st
# from datetime import date
# from PIL import Image
# import requests
# from io import BytesIO

# # Page Configuration
# st.set_page_config(
#     page_title="Industry Demos",
#     page_icon="",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Title and Horizontal Line
# st.markdown(
#     """
#     <style>
#     .custom-title {
#         color: #333;  /* Saffron yellow color */
#         font-size: 36px;
#         font-weight: bold;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Display the title with custom styling
# st.markdown('<p class="custom-title">Industry Demos </p>', unsafe_allow_html=True)
# st.write("Current Date:", date.today())
# st.markdown("""<hr style="height:2px;border:none;color:#F4C430;background-color:#3333" /> """,
#             unsafe_allow_html=True)

# # State to toggle expand/collapse
# if 'expand_all' not in st.session_state:
#     st.session_state.expand_all = False


# def toggle_expand():
#     st.session_state.expand_all = not st.session_state.expand_all


# # Maximize/Collapse All Button
# st.button("Maximize/Collapse All", on_click=toggle_expand)

# # Widget URLs
# widget_urls = [
#     {"name":"Dynamics-CustomerInsights","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
#     {"name":"Fabric","url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
#     {"name": "Retail Industry", "url": "https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Retail%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Finance Industry","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Financial%20Services%20Industry%20DREAM%20Demo"},
#     {"name":"Manufacturing Industry","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Manufacturing%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Healthcare Industry - BDM","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"},
#     {"name":"Healthcare Industry - TDM","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
#     {"name":"Healthcare Industry - V1","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Healthcare%20Industry%20Scenario%20DREAM%20Demo"},
#     {"name":"Sustainability","url":"https://app-sustainabilitydemo-prod.azurewebsites.net/#/login"},
#     {"name":"Public Finance","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
#     {"name":"Public Finance Full Demo","url":"https://content.cloudguides.com/en-us/guides/Data%20and%20AI%20Public%20Finance%20Industry%20DREAM%20Demo%20-%20BDM"},
   
#     {"name":"Consumer Goods DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2249/consumer-goods-dream-demo/index.html#/0/0"},
#     {"name":"Healthcare DREAM demo for TDM","url":"https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
#     {"name":"Customer Insights for Retail Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
#     {"name":"Customer Insights for Financial Services Industry - DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2218/customer-insights-for-financial-services-industry-dream-demo/index.html#/0/0"},
#     {"name":"Healthcare Industry Scenario Dream Demo","url":"https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"}
   


# ]




# # Columns
# cols = st.columns(3)

# # Custom JavaScript for modal functionality
# st.markdown(
#     """
#     <script>
#     function openModal(url) {
#         var modal = document.getElementById("myModal");
#         var iframe = document.getElementById("modalIframe");
#         iframe.src = url;
#         modal.style.display = "block";
#     }

#     function closeModal() {
#         var modal = document.getElementById("myModal");
#         var iframe = document.getElementById("modalIframe");
#         iframe.src = "";
#         modal.style.display = "none";
#     }
#     </script>
#     """,
#     unsafe_allow_html=True
# )

# # HTML for modal
# st.markdown(
#     """
#     <div id="myModal" class="modal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.5);">
#         <div class="modal-content" style="background-color: #fff; margin: 5% auto; padding: 20px; border: 1px solid #888; width: 90%; max-width: 900px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
#             <span class="close" onclick="closeModal()" style="color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer;">&times;</span>
#             <iframe id="modalIframe" src="" style="width: 100%; height: 70vh; border: none; border-radius: 8px;"></iframe>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Placeholder image URL
# # Use a valid placeholder URL
# placeholder_img_url = "https://via.placeholder.com/300"

# # # Widget containers
# # for i, widget in enumerate(widget_urls):
# #     with cols[i % 3]:
# #         # Display widget name as a clickable link that opens in a new window
# #         st.markdown(f'''
# #             <div style="text-align: center; margin-bottom: 10px;">
# #                 <a href="{widget['url']}" target="_blank" style="text-decoration: none; color: #158237; font-weight: bold; font-size: 14px;">
# #                     {widget['name']}
# #                 </a>
# #             </div>
# #         ''', unsafe_allow_html=True)

# #         # Expander with content
# #         with st.expander("", expanded=st.session_state.expand_all):
# #             try:
# #                 st.markdown(f'''
# #                     <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
# #                         <iframe src="{widget['url']}" width="100%" height="100%" scrolling="yes" frameborder="0" allowfullscreen style="border: none; border-radius: 12px;"></iframe>
# #                     </div>
# #                 ''', unsafe_allow_html=True)
# #             except:
# #                 # Display placeholder image if iframe cannot be loaded
# #                 st.markdown(f'''
# #                     <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
# #                         <img src="{placeholder_img_url}" alt="Preview Not Available" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
# #                     </div>
# #                 ''', unsafe_allow_html=True)

# # new widget code


# # Initialize session state attributes if they don't exist
# if 'maximized_widget' not in st.session_state:
#     st.session_state.maximized_widget = None
# if 'expand_all' not in st.session_state:
#     st.session_state.expand_all = False

# # Function to handle maximizing an iframe


# def toggle_maximize(widget_name):
#     if st.session_state.maximized_widget == widget_name:
#         st.session_state.maximized_widget = None
#     else:
#         st.session_state.maximized_widget = widget_name


# # Columns layout
# cols = st.columns(3)

# # Placeholder image URL
# placeholder_img_url = "https://via.placeholder.com/300"

# # Custom CSS for styling and responsiveness
# st.markdown(
#     """
#     <style>
#     .overlay {
#         display: none;
#         position: fixed;
#         z-index: 1000;
#         left: 0;
#         top: 0;
#         width: 100%;
#         height: 100%;
#         overflow: auto;
#         background-color: rgba(0,0,0,0.8);
#         transition: opacity 0.3s ease;
#     }
#     .overlay.active {
#         display: block;
#         opacity: 1;
#     }
#     .iframe-container {
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-50%, -50%);
#         width: 90%;
#         height: 90%;
#         background-color: #fff;
#         border: 1px solid #888;
#         border-radius: 12px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         display: flex;
#         flex-direction: column;
#         padding: 10px;
#         box-sizing: border-box;
#     }
#     .refresh-btn, .close-btn, .back-link {
#         position: absolute;
#         background: none;
#         border: none;
#         color: #007bff;
#         cursor: pointer;
#         font-size: 18px;
#         padding: 10px;
#         border-radius: 5px;
#         transition: background 0.2s ease;
#     }
#     .refresh-btn {
#         top: 10px;
#         right: 10px;
#         background: #007bff;
#         color: white;
#     }
#     .refresh-btn:hover {
#         background: #0056b3;
#     }
#     .close-btn {
#         top: 10px;
#         left: 10px;
#         font-size: 28px;
#         color: #aaa;
#     }
#     .close-btn:hover {
#         color: black;
#     }
#     .back-link {
#         position: absolute;
#         bottom: 10px;
#         left: 50%;
#         transform: translateX(-50%);
#         background: #fff;
#         color: #007bff;
#         font-size: 18px;
#         padding: 10px;
#         border: 1px solid #007bff;
#         border-radius: 5px;
#         text-decoration: none;
#         display: block;
#     }
#     .back-link:hover {
#         background: #007bff;
#         color: white;
#     }
#     @media only screen and (max-width: 768px) {
#         .iframe-container {
#             width: 100%;
#             height: 100%;
#             padding: 5px;
#         }
#         .refresh-btn, .close-btn, .back-link {
#             font-size: 16px;
#             padding: 8px;
#         }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Widget containers
# for i, widget in enumerate(widget_urls):
#     with cols[i % 3]:
#         # Display widget name as a clickable link that opens in a new window
#         st.markdown(f'''
#             <div style="text-align: center; margin-bottom: 10px;">
#                 <a href="{widget['url']}" target="_blank" style="text-decoration: none; color: #333; font-weight: bold; font-size: 14px;">
#                     {widget['name']}
#                 </a>
#             </div>
#         ''', unsafe_allow_html=True)

#         # Expander with content
#         with st.expander("", expanded=st.session_state.expand_all):
#             # Button to maximize the iframe
#             st.button("Maximize", on_click=toggle_maximize, args=(
#                 widget['name'],), key=f"maximize-{widget['name']}")

#             if st.session_state.maximized_widget == widget['name']:
#                 # Display the overlay for the maximized widget
#                 st.markdown(
#                     f"""
#                     <div class="overlay active">
#                         <div class="iframe-container">
#                             <button class="refresh-btn" onclick="window.location.reload();">Refresh the Browser to back to Home page</button>
#                             <button class="close-btn" onclick="window.location.reload();">×</button>
#                             <iframe src="{widget['url']}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
#                             <a href="#" class="back-link" onclick="window.location.reload();"> </a>
#                         </div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#             else:
#                 try:
#                     st.markdown(f'''
#                         <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
#                             <iframe src="{widget['url']}" width="100%" height="100%" scrolling="yes" frameborder="0" allowfullscreen style="border: none; border-radius: 12px;"></iframe>
#                         </div>
#                     ''', unsafe_allow_html=True)
#                 except:
#                     # Display placeholder image if iframe cannot be loaded
#                     st.markdown(f'''
#                         <div style="position: relative; width: 100%; height: 300px; padding: 5px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
#                             <img src="{placeholder_img_url}" alt="Preview Not Available" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
#                         </div>
#                     ''', unsafe_allow_html=True)


# # Custom CSS for styling and responsiveness
# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://images.unsplash.com/photo-1682685797857-97de838c192e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3387&q=80");
#         background-size: cover;
#         padding: 0 20px;
#     }
#     .sidebar .sidebar-content {
#         background: url("");
#     }
#     .st-expander {
#         margin-bottom: 20px;
#         border: 1px solid #158237;
#         border-radius: 12px;
#         background-color: #fff;
#     }
#     .st-expander__header {
#         display: none;
#     }
#     .st-expander__content {
#         padding: 0;
#     }
#     a {
#         text-decoration: none;
#     }
#     a:hover {
#         color: #0d6a3b;
#     }
#     iframe {
#         border-radius: 12px;
#         padding: 0; /* Ensure no extra padding around iframe */
#     }
#     .modal {
#         display: none; 
#         position: fixed; 
#         z-index: 1000; 
#         left: 0; 
#         top: 0; 
#         width: 100%; 
#         height: 100%; 
#         overflow: auto; 
#         background-color: rgba(0,0,0,0.5); 
#     }
#     .modal-content {
#         background-color: #fff; 
#         margin: 5% auto; 
#         padding: 20px; 
#         border: 1px solid #888; 
#         width: 90%; 
#         max-width: 900px; 
#         border-radius: 12px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
#     .close {
#         color: #aaa;
#         float: right;
#         font-size: 28px;
#         font-weight: bold;
#         cursor: pointer;
#     }
#     .close:hover,
#     .close:focus {
#         color: black;
#         text-decoration: none;
#         cursor: pointer;
#     }
#     @media only screen and (max-width: 768px) {
#         iframe {
#             height: calc(100vw / 1.5) !important;
#         }
#         .st-expander {
#             width: 100%;
#         }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True



# )
