# import streamlit as st
# from PIL import Image
# import requests
# from io import BytesIO
# from datetime import date


# #title

# # Page Configuration
# st.set_page_config(
#     page_title="Architecture Diagrams",
#     page_icon="",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Title and Horizontal Line

# st.markdown(
#     """
#     <style>
#     .custom-title {
#         color: #324ab2;  /* Voilet */
#         font-size: 40px;
#         font-weight: bold;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Display the title with custom styling
# st.markdown('<p class="custom-title">Architecture Diagrams </p>', unsafe_allow_html=True)
# st.write("Current Date:", date.today()) 
# st.markdown("""<hr style="height:2px;border:none;color:#324ab2;background-color:#324ab2;" /> """,
#             unsafe_allow_html=True)






# # Professional business images for the carousel with names
# images = [
#     {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/daidemo_fabric_3_demo_arch_V2.gif", "name": "Fabric Demo Architecture 3.0"},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/fabric_2_demo_arch.gif", "name": "Fabric Demo Architecture 2.0"},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/snowflake/snowflake_demo_architecture.png", "name": "Snowflake Demo Architecture"},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/Fabric_ADB_Architecture_Diagram.gif", "name": "Fabric Azure Databricks Architecture "},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/purview_demo_arch_4.png", "name": "Purview Demo Architecture"},
#     {"url": "https://nrfcdn.azureedge.net/fab_db_2_arch_diagram.gif", "name": "Microsoft Fabric Databricks 2.0 Architecture"},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/manufacturing/Mfg_with_fabric_arch_1.gif", "name": "Manufacturing with Fabric Architecture"},
#     {"url": "https://dreamdemoassets.blob.core.windows.net/nrf/Fabric_AML_Arc.png", "name": "Fabric Azure AML Architecture"},
#     {"url": "https://nrfcdn.azureedge.net/mfdb2_onelake_architecture.png", "name": "Microsoft Fabric Databricks 2.0 Onelake Architecture"},
#     {"url": "https://nrfcdn.azureedge.net/mfigdb_onelake_architecture.gif", "name": "Microsoft Fabric Databricks  Onelake Architecture"},
# ]

# # Initialize session state for the current image index
# if 'current_index' not in st.session_state:
#     st.session_state.current_index = 0

# # Function to display the current image and name
# def display_image(index):
#     response = requests.get(images[index]["url"])
#     img = Image.open(BytesIO(response.content))
#     st.image(img, use_column_width=True)
#     st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 18px;'>{images[index]['name']}</p>", unsafe_allow_html=True)

# # Custom CSS for responsive design and arrows on the sides of the carousel
# st.markdown(
#     """
#     <style>
#     .carousel-container {
#         position: relative;
#         width: 50%;
#         max-width: 50%;
#         margin: auto;
#         overflow: hidden;
#         background-image: url("{images[st.session_state.current_index]['url']}");
#         background-size: cover;
#         background-position: center;
#         border-radius: 10px;
#     }
#     .carousel-container img {
#         width: auto;
#         height: auto;
#         display: block;
#     }
#     .arrow-left, .arrow-right {
#         position: sticky;
#         botton: 50%;
#         transform: translateY(-50%);
#         background-color: rgba(0, 0, 0, 0.5);
#         color: white;
#         border: none;
#         padding: 10px;
#         cursor: pointer;
#         border-radius: 50%;
#         font-size: 20px;
#         z-index: 10;
#     }
#     .arrow-left {
#         left: 15px;
#     }
#     .arrow-right {
#         right: 15px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Display the carousel container with overlaid arrows
# st.markdown('<div class="carousel-container">', unsafe_allow_html=True)

# # Left arrow button
# if st.button("◀", key="prev", help="Previous Image"):
#     st.session_state.current_index = (st.session_state.current_index - 1) % len(images)

# # Display the current image and name
# display_image(st.session_state.current_index)

# # Right arrow button
# if st.button("▶", key="next", help="Next Image"):
#     st.session_state.current_index = (st.session_state.current_index + 1) % len(images)

# st.markdown('</div>', unsafe_allow_html=True)

# # Optional content below the carousel

# st.markdown("Navigate through the images using the arrows.")