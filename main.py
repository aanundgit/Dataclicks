import streamlit as st
from datetime import date, timedelta
# from streamlit_extras.colored_header import colored_header
import pytz


st.set_page_config(
    page_title="",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://aka.ms/dreams',

    }
)
st.title('DEMO-:blue[Sites 🌎]')
st.markdown(date.today())



#Top Navigation 


def top_navigation():
    st.markdown("""
    <style>
    .topnav {
        background-color: #f5f5f5;
        overflow: hidden;
        color: white;
    }
    
    .topnav a {
        float: left;
        display: block;
        color: #333;
        text-align: center;
        padding: 12px 14px;
        text-decoration: none;
        font-size: 15px;
    }
    
    .topnav a:hover {
        background-color: #ddd;
        color: black;
    }
    
    .topnav a.active {
        background-color: #333;
        color: white;
    }
    </style>
    
    <div class="topnav">
        <a class="active" href="#home">Home</a>
        <a href="https://blog.fabric.microsoft.com/en-US/blog/" target="_blank">Microsoft Fabric Blog</a>
        <a href="https://www.microsoft.com/en-us/microsoft-fabric/partners" target="_blank">Microsoft Fabric Partners</a>
        <a href="https://powerbi.microsoft.com/en-us/blog/" target="_blank">Microsoft Power BI Blog</a>
        <a href="https://app.powerbi.com" target="_blank">Power BI</a>
        <a href="https://github.com/microsoft/Azure-Analytics-and-AI-Engagement" target="_blank">GitHub</a>
        <a href="https://partner.microsoft.com/en-us/asset/collection/industry-dream-demos-and-dream-demo-in-a-box#/" target="_blank">Partner Portal</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Top navigation bar
top_navigation()
st.markdown("""<hr style="height:2px;border:none;color:#1c83e1;background-color:#1c83e1;" /> """,
            unsafe_allow_html=True)


# current_date = date.today()


# colored_header(
#    label = "" ,
#    description =" This page shows anavar's Embedded Pages",
#    color_name = "blue-70")
#
# st.components.v1.iframe("https://aanundgit.github.io/varanadays-drop/", width=800, height=600)
# st.components.v1.iframe("https://app.powerbi.com", width=800, height=600)


# def auto_fit_containers():
#     """Creates responsive columns with iframes and handles potential width issues."""

#     col1, col2, col3 = st.columns(3)  # Create three columns

#     with col1:
#         st.write("**Days Counter**")  # Add a title or description for clarity
#         st.components.v1.iframe(
#             "https://blog.fabric.microsoft.com/en-US/blog/", width=None, height=400)

#     with col3:
#         # Add a title or description for clarity
#         st.write("**Power BI Scanner**", "**https://pbiscanner.onrender.com**")
#         st.components.v1.iframe(
#             "https://pbiscanner.onrender.com", width=None, height=400)


# Call the function to display the layout
# auto_fit_containers()

# st.write(today,tzinfo= pytz.all_timezonestzinfo=pytz.timezone("EST"))
# current_date = datetime.today()
# current_month = current_date
# st.markdown(''':blue[Dream Demos]''')
# Define the URLs of the apps you want to embed
widget_urls = [
    # {"name": "Open-AI", "url": "https://open.ai"},
    {"name": "Microsoft Fabric Guided Tour",
        "url": "https://guidedtour.microsoft.com/en-us/guidedtour/microsoft-fabric/microsoft-fabric/1/1"},
    {"name": "Microsoft Power BI Guided Tour",
        "url": "https://guidedtour.microsoft.com/en-us/guidedtour/power-platform/power-bi/1/1"},
    {"name": "Fabric Partners",
        "url": "https://www.microsoft.com/en-us/microsoft-fabric/partners"},
    {"name": "Dream Demos Partner", "url": "https://partner.microsoft.com/en-us/asset/collection/industry-dream-demos-and-dream-demo-in-a-box#/"}    
   

]

# Set the height of the embedded widgets
widget_height = 285

# Display the current date and time in the sidebar
# st.sidebar.markdown(f"Current Date: {current_date.strftime('%Y-%m-%d')}")
# st.sidebar.markdown(f"Current Time: {current_date.strftime('%H:%M:%S')}")
#old code for sidebar

# with st.sidebar:
#     listedSkills = st.expander("Skillset")
#     with listedSkills:
#         st.write( 
#             """
#         * Azure
#         * aws
#         * GCP
#         * Snowflake
#         * PowerBI
#         * Python
#         * Datawarehousing
#         * Data Analysis
#         * Delta Lake
#         * Apache Spark
#         * Databricks
#         * Azure Synapse Analytics
#         * Dynamics365
#         * R
#         * RDBMS
#         * NoSQLDB
#         * DAX
#         * PowerQuery
#         * SQL
#         * PowerShell
#         * Bash
#         * Program Management
#         * Project Management
#         * Excel
#         * Product Management
#         * Data Mesh
#         * SDLC
#         * Scala
#         * Azure DevOps
#         * Leadership
        
#         [Website](https://aka.ms/dreams)
#         """
#         )


# New Code for sidebar links



# Sidebar with clickable links
with st.sidebar:
    listedSkills = st.expander("Useful Links")
    with listedSkills:
        st.write("")
        
        # Define your list of links
        links = [
            {"name": "Azure Portal", "url": "https://www.portal.azure.com"},
            {"name": "Power BI", "url": "https://app.powerbi.com"},
            {"name": " ", "url": " "},
            {"name": " ", "url": " "},
        ]
        
        # Generate clickable links
        for link in links:
            st.markdown(f'<a href="{link["url"]}" target="_blank">{link["name"]}</a>', unsafe_allow_html=True)


# Display the calendar widget in the sidebar
# selected_date = st.sidebar.date_input("Date Picker")

# Display the current month
# st.write(f": **{current_date}**")

# Create expandable containers for the embedded widgets
# for widget in widget_urls:
#     with st.expander(widget["name"], expanded=False):
#         st.markdown(f"[{widget['url']}]({widget['url']})")
#         st.markdown(
#             f'<iframe src="{widget["url"]}" width="100%" height="{widget_height}" scrolling="yes" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
# #-------------------------------------------------



# new code for widget to load image of the website. 



# State to store the current maximized widget
if 'maximized_widget' not in st.session_state:
    st.session_state.maximized_widget = None

def toggle_overlay(widget=None):
    if widget:
        st.session_state.maximized_widget = widget
    else:
        st.session_state.maximized_widget = None

# Custom CSS for the overlay
st.markdown("""
    <style>
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.8);
        z-index: 1000;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .iframe-container {
        width: 80%;
        height: 80%;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        position: relative;
    }
    .close-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .back-link {
        display: block;
        text-align: center;
        margin-top: 20px;
        color: #007bff;
        font-size: 16px;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the widgets in three columns
cols = st.columns(3)

for i, widget in enumerate(widget_urls):
    with cols[i % 3].expander(widget["name"], expanded=False):
        # The title is now a clickable link
        st.markdown(f'<a href="{widget["url"]}" target="_blank" style="font-size:18px; font-weight:bold; text-decoration:none; color:#007bff;">{widget["name"]}</a>', unsafe_allow_html=True)
        
        # Display the iframe in default size
        st.markdown(
            f'<iframe src="{widget["url"]}" width="100%" height="300" frameborder="0" allowfullscreen></iframe>',
            unsafe_allow_html=True
        )
        
        # Button to maximize the iframe
        st.button("Maximize", on_click=toggle_overlay, args=(widget,), key=f"maximize-{widget['name']}")

# Display the overlay if a widget is maximized
if st.session_state.maximized_widget:
    widget = st.session_state.maximized_widget
    st.markdown(
        f"""
        <div class="overlay">
            <div class="iframe-container">
                <button class="close-btn" onclick="window.location.reload();">Close</button>
                <iframe src="{widget['url']}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
                <a href="#" class="back-link" onclick="window.location.reload();">Back to Home</a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
