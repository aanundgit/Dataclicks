import streamlit as st
from datetime import date
from PIL import Image
import requests
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="All Click by Click Demos",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title and Horizontal Line
st.title(":blue[All Click by Click Demos]")
st.write("Current Date:", date.today())
st.markdown("""<hr style="height:2px;border:none;color:#317ae8;background-color:#317ae8;" /> """,
            unsafe_allow_html=True)

# State to toggle expand/collapse
if 'expand_all' not in st.session_state:
    st.session_state.expand_all = False


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
    {"name": "Azure OpenAI Service Dream Demo for FSI",
        "url": "https://regale.cloud/Microsoft/viewer/2723/azure-openai-service-dream-demo-for-fsi/index.html#/0/0"},
    {"name": "Microsoft Fabric with Azure Machine Learning Dream Demo TDM+BDM",
        "url": "https://regale.cloud/Microsoft/viewer/2705/microsoft-fabric-with-azure-machine-learning-dream-demo/index.html#/0/0"},
    {"name": "PowerBI Differentiators Demo",
        "url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric end-to-end demo",
        "url": "https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
    {"name": "Modern Analytics with Microsoft Fabric and Azure Databricks DREAM Lab",
        "url": "https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
    {"name": "Modern Analytics with Azure Databricks and Power BI DREAM Demo (Partners)",
     "url": "https://regale.cloud/Microsoft/viewer/2426/partners-modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name": "Modern Analytics with Azure Databricks and Power BI DREAM Demo",
        "url": "https://regale.cloud/Microsoft/viewer/2421/modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name": "CosmosDB + OpenAI DREAM Demo",
        "url": "https://regale.cloud/Microsoft/viewer/2493/cosmosdb-openai-dream-demo/index.html#/0/0"},
    {"name": "Azure OpenAI Service Dream demo with shopping co-pilot.",
        "url": "https://regale.cloud/Microsoft/viewer/2486/azure-openai-service-dream-demo-with-shopping-co-pilot/index.html#/0/0"},
    {"name": "Azure OpenAI Service Dream Demo 10-minute",
        "url": "https://regale.cloud/Microsoft/viewer/2383/azure-openai-service-dream-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric Dream Demo (10 minute)",
     "url": "https://regale.cloud/Microsoft/viewer/2466/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric Dream Demo (5 minute)",
     "url": "https://regale.cloud/Microsoft/viewer/2411/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric DREAM Demo (4 Minute) PARTNERS",
     "url": "https://regale.cloud/Microsoft/viewer/2427/partners-microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric DREAM Demo (4 Minute)",
     "url": "https://regale.cloud/Microsoft/viewer/2379/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": "Azure OpenAI Service Dream Demo (with admin tool) 10-minute",
     "url": "https://regale.cloud/Microsoft/viewer/2376/azure-openai-service-dream-demo-with-admin-tool/index.html#/0/0"},
    {"name": "Microsoft Fabric Embedded Demo",
        "url": "https://regale.cloud/Microsoft/viewer/2262/microsoft-fabric-embedded-demo/index.html#/0/0"},
    {"name": "Microsoft Fabric and Azure Databricks DREAM Demo",
        "url": "https://simdemo.azureedge.net/dai/fabric-databricks/index.html#/0/0"},
    {"name": "Microsoft Fabric and Azure Databricks DREAM Demo (Partners)",
     "url": "https://regale.cloud/Microsoft/viewer/2428/partners-microsoft-fabric-and-azure-databricks-dream-demo/index.html#/0/0"},
    {"name": "Azure Databricks and Microsoft Fabric DREAM Demo (booth)",
     "url": "https://regale.cloud/Microsoft/viewer/2303/azure-databricks-and-microsoft-fabric-dream-demo-booth/index.html#/0/0"},
    {"name": "Power BI Differentiators Dream Demo Full Click by Click",
        "url": "https://regale.cloud/Microsoft/viewer/instance/2053/6338/index.html#/0/0"},
    {"name": "Analytics in MIDP Dream Demo for BDMs",
        "url": "https://regale.cloud/Microsoft/viewer/2006/analytics-in-midp-dream-demo-for-bdms/index.html#/0/0"},
    {"name": "Power BI Differentiators Dream Demo Full Click by Click V2","url": "https://regale.cloud/Microsoft/viewer/1947/power-bi-differentiators-dream-demo-integrated-into-web-app/index.html#/0/0"},
    {"name": "Azure OpenAI Service DREAM Demo (with admin tool) 10-minute","url": "https://regale.cloud/Microsoft/viewer/2376/azure-openai-service-dream-demo-with-admin-tool/index.html#/0/0"},
    {"name": ":Demo1 :", "url": "https://regale.cloud/Microsoft/viewer/1947/power-bi-differentiators-dream-demo-integrated-into-web-app/index.html#/0/0"},
    {"name": ":Demo2 :", "url": "https://regale.cloud/Microsoft/viewer/2006/analytics-in-midp-dream-demo-for-bdms/index.html#/0/0"},
    {"name": ":Demo3 :", "url": "https://regale.cloud/Microsoft/viewer/instance/2053/6338/index.html#/0/0"},
    {"name": ":Demo4 :", "url": "https://regale.cloud/Microsoft/viewer/2111/power-bi-differentiators-dream-demo-full-click-by-click-v2-draft/index.html#/0/0"},
    {"name": ":Demo5 :", "url": "https://regale.cloud/Microsoft/viewer/2214/healthcare-dream-demo-for-bdm/index.html#/0/0"},
    {"name": ":Demo6 :", "url": "https://regale.cloud/Microsoft/viewer/2217/customer-insights-for-retail-industry-dream-demo/index.html#/0/0"},
    {"name": ":Demo7 :", "url": "https://regale.cloud/Microsoft/viewer/2218/customer-insights-for-financial-services-industry-dream-demo/index.html#/0/0"},
    {"name": ":Demo8 :", "url": "https://regale.cloud/Microsoft/viewer/2221/healthcare-dream-demo-for-tdm/index.html#/0/0"},
    {"name": ":Demo9 :", "url": "https://regale.cloud/Microsoft/viewer/2249/consumer-goods-dream-demo/index.html#/0/0"},
    {"name": ":Demo10: ", "url": "https://regale.cloud/Microsoft/viewer/2262/microsoft-fabric-embedded-demo/index.html#/0/0"},
    {"name": ":Demo11:", "url": "https://regale.cloud/Microsoft/viewer/2303/azure-databricks-and-microsoft-fabric-dream-demo-booth/index.html#/0/0"},
    {"name": ":Demo12:", "url": "https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
    {"name": ":Demo13:", "url": "https://regale.cloud/Microsoft/viewer/2376/azure-openai-service-dream-demo-with-admin-tool/index.html#/0/0"},
    {"name": ":Demo14:", "url": "https://regale.cloud/Microsoft/viewer/2379/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": ":Demo15:", "url": "https://regale.cloud/Microsoft/viewer/2383/azure-openai-service-dream-demo/index.html#/0/0"},
    {"name": ":Demo16:", "url": "https://regale.cloud/Microsoft/viewer/2411/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": ":Demo17:", "url": "https://regale.cloud/Microsoft/viewer/2421/modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name": ":Demo18:", "url": "https://regale.cloud/Microsoft/viewer/2426/partners-modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
    {"name": ":Demo19:", "url": "https://regale.cloud/Microsoft/viewer/2427/partners-microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": ":Demo20:", "url": "https://regale.cloud/Microsoft/viewer/2428/partners-microsoft-fabric-and-azure-databricks-dream-demo/index.html#/0/0"},
    {"name": ":Demo21:", "url": "https://simdemo.azureedge.net/dai/fabric-databricks/index.html#/0/0"},
    {"name": ":Demo22:", "url": "https://regale.cloud/Microsoft/viewer/2466/microsoft-fabric-dream-demo/index.html#/0/0"},
    {"name": ":Demo23:", "url": "https://regale.cloud/Microsoft/viewer/2486/azure-openai-service-dream-demo-with-shopping-co-pilot/index.html#/0/0"},
    {"name": ":Demo24:", "url": "https://regale.cloud/Microsoft/viewer/2493/cosmosdb-openai-dream-demo/index.html#/0/0"},
    {"name": ":Demo25:", "url": "https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
    {"name": ":Demo26:", "url": "https://regale.cloud/Microsoft/viewer/2705/microsoft-fabric-with-azure-machine-learning-dream-demo/index.html#/0/0"},
    {"name": ":Demo27:", "url": "https://regale.cloud/Microsoft/viewer/2723/azure-openai-service-dream-demo-for-fsi/index.html#/0/0"},
    {"name": ":Demo28:", "url": "https://regale.cloud/Microsoft/viewer/2772/microsoft-fabric-and-copilot-for-power-bi/index.html#/0/0"},
    {"name": ":Demo29:", "url": "https://regale.cloud/Microsoft/viewer/2777/intelligent-apps-azure-cosmos-db-and-azure-openai-dream-demo-bdm-tdm/index.html#/0/0"},
    {"name": ":Demo30:", "url": "https://regale.cloud/Microsoft/viewer/2852/microsoft-fabric-20-dream-demo/index.html#/0/0"},
    {"name": ":Demo31:", "url": "https://regale.cloud/Microsoft/viewer/2857/education-dream-demo-bdm/index.html#/0/0"},
    {"name": ":Demo32:", "url": "https://regale.cloud/Microsoft/viewer/2919/copilot-for-power-bi-in-microsoft-fabric-presenter-view-portuguese-version/index.html#/0/0"},
    {"name": ":Demo33:", "url": "https://regale.cloud/Microsoft/viewer/2938/modern-analytics-with-azure-databricks-21/index.html#/0/0"},
    {"name": ":Demo34:", "url": "https://regale.cloud/Microsoft/viewer/2939/copilot-for-power-bi-in-microsoft-fabric-dream-demo-presenter-view-english-versi/index.html#/0/0"},
    {"name": ":Demo35:", "url": "https://regale.cloud/Microsoft/viewer/2940/modern-analytics-with-azure-databricks-22-power-bi-version/index.html#/0/0"},
    {"name": ":Demo36:", "url": "https://regale.cloud/Microsoft/viewer/2961/education-dream-demo-bdm-partners/index.html#/0/0"},
    {"name": ":Demo37:", "url": "https://regale.cloud/Microsoft/viewer/2968/copilot-for-power-bi-in-microsoft-fabric-dream-demo-presenter-view-english-germa/index.html#/0/0"},
    {"name": ":Demo38:", "url": "https://regale.cloud/Microsoft/viewer/2976/copilot-for-power-bi-in-microsoft-fabric-dream-demo-presenter-view-english-itali/index.html"},
    {"name": ":Demo39:", "url": "https://regale.cloud/Microsoft/viewer/3004/copilot-for-power-bi-in-microsoft-fabric-manufacturing-hmi-dream-demo-backend-on/index.html#/0/0"},
    {"name": ":Demo40:", "url": "https://regale.cloud/Microsoft/viewer/3010/copilot-for-power-bi-in-microsoft-fabric-manufacturing-hmi-dream-demo-full-demo/index.html#/0/0"},
    {"name": ":Demo41:", "url": "https://regale.cloud/Microsoft/viewer/3023/copilot-for-power-bi-in-microsoft-fabric-manufacturing-dream-demo-backend-copilo/index.html#/0/0"},
    {"name": ":Demo42:", "url": "https://regale.cloud/Microsoft/viewer/3050/rag-databricks/index.html#/0/0"},
    {"name": ":Demo43:", "url": "https://regale.cloud/Microsoft/viewer/3063/task-21-explore-delta-live-table-pipeline-data-transformation/index.html#/0/0"},
    {"name": ":Demo44:", "url": "https://regale.cloud/Microsoft/viewer/3066/task-22-explore-the-data-in-azure-databricks-environment-with-unity-catalog/index.html#/0/0"},
    {"name": ":Demo45:", "url": "https://regale.cloud/Microsoft/viewer/3073/task-13-use-the-new-shortcut-option-from-external-data-sources/index.html#/0/0"},
    {"name": ":Demo46:", "url": "https://regale.cloud/Microsoft/viewer/3074/task-11-use-the-data-pipelines-data-flow-no-code-low-code-experience/index.html#/0/0"},
    {"name": ":Demo47:", "url": "https://regale.cloud/Microsoft/viewer/3075/task-31-create-semantic-model-and-generate-insights-using-copilot-for-power-bi/index.html#/0/0"},
    {"name": ":Demo48:", "url": "https://regale.cloud/Microsoft/viewer/3078/task-12-transform-data-using-dataflow-gen2-no-code-low-code-experience-copilot/index.html#/0/0"},
    {"name": ":Demo49:", "url": "https://regale.cloud/Microsoft/viewer/3079/task-41-ingest-real-time-historical-data-into-kql-db-using-eventstream/index.html#/0/0"},
    {"name": ":Demo50:", "url": "https://regale.cloud/Microsoft/viewer/3084/task-42-analyze-discover-patterns-identify-anomalies-and-outliers-using-copilot/index.html#/0/0"},
    {"name": ":Demo51:", "url": "https://regale.cloud/Microsoft/viewer/3085/task-51-build-ml-models-experiments-and-log-ml-model-in-the-built-in-model-regis/index.html#/0/10"},
    {"name": ":Demo52:", "url": "https://regale.cloud/Microsoft/viewer/3088/modern-analytics-with-microsoft-fabric-copilot-and-azure-databricks-dream-lab-fu/index.html#/0/0"},
    {"name": ":Demo53:", "url": "https://regale.cloud/Microsoft/viewer/3176/snowflake-dream-demo-bdm/index.html#/0/0"},
    {"name": ":Demo54:", "url": "https://regale.cloud/Microsoft/viewer/3189/azure-openai-dream-demo-for-fis/index.html#/0/0"},
    {"name": ":Demo55:", "url": "https://regale.cloud/Microsoft/viewer/3247/microsoft-fabric-databricks-20/index.html#/0/0"},
    {"name": ":Demo56:", "url": "https://regale.cloud/Microsoft/play/3273/sustainability-20-dream-demo#/0/0"},
    {"name": ":Demo57:", "url": "https://regale.cloud/microsoft/play/3306/better-together-microsoft-fabric-with-azure-ai-studio-dream-demo#/:0/:0"}








]

# Filter widgets based on search query
filtered_widget_urls = [widget for widget in widget_urls if st.session_state.search_query.lower() in widget['name'].lower()]

# Placeholder image URL
placeholder_img_url = "https://via.placeholder.com/300"

# Initialize session state attributes if they don't exist
if 'maximized_widget' not in st.session_state:
    st.session_state.maximized_widget = None





# Function to handle maximizing an iframe


def toggle_maximize(widget_name):
    if st.session_state.maximized_widget == widget_name:
        st.session_state.maximized_widget = None
    else:
        st.session_state.maximized_widget = widget_name


# Custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
    }
    .stButton button {
        width: 100%;
        background-color: #317ae8;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #0d6a3b;
    }
    .st-expander {
        border: 1px solid #317ae8;
        border-radius: 12px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }
    .st-expander__header {
        font-size: 1.1em;
        font-weight: bold;
        color: #158237;
        padding: 10px 0;
        text-align: center;
    }
    .st-expander__content {
        padding: 0 10px 10px 10px;
    }
    .iframe-container {
        position: relative;
        width: 100%;
        padding-top: 56.25%;
        margin-bottom: 10px;
    }
    .iframe-container iframe {
        position: absolute;
        top: 0;
        left: 0;
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
    }
    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    @media (max-width: 768px) {
        .modal-content {
            width: 95%;
        }
        .iframe-container {
            padding-top: 75%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Placeholder function to render iframes or images


def render_iframe_or_image(url, height='300px'):
    try:
        st.markdown(f'''
            <div class="iframe-container" style="height: {height};">
                <iframe src="{url}" frameborder="0" allowfullscreen></iframe>
            </div>
        ''', unsafe_allow_html=True)
    except:
        st.image(placeholder_img_url, caption="Preview Not Available")


# Two-column layout for widget containers
col1, col2 = st.columns(2)
columns = [col1, col2]
current_col = 0

for i, widget in enumerate(widget_urls):
    with columns[current_col].expander(widget['name'], expanded=st.session_state.expand_all):
        st.button("Maximize", on_click=toggle_maximize, args=(
            widget['name'],), key=f"maximize-{widget['name']}")

        if st.session_state.maximized_widget == widget['name']:
            # Display the modal for the maximized widget
            st.markdown(
                f"""
                <div class="modal" style="display:block;">
                    <div class="modal-content" style="width: 95%; max-width: 1200px;">
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


# --------------------------------------------------old code with three column format ----------------------------
# import streamlit as st
# from datetime import date
# from PIL import Image
# import requests
# from io import BytesIO

# # Page Configuration
# st.set_page_config(
#     page_title="Product Demos",
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
# st.markdown('<p class="custom-title">Product Demos </p>', unsafe_allow_html=True)
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
#     {"name":"Azure OpenAI Service Dream Demo for FSI","url":"https://regale.cloud/Microsoft/viewer/2723/azure-openai-service-dream-demo-for-fsi/index.html#/0/0"},
#     {"name":"Microsoft Fabric with Azure Machine Learning Dream Demo TDM+BDM","url":"https://regale.cloud/Microsoft/viewer/2705/microsoft-fabric-with-azure-machine-learning-dream-demo/index.html#/0/0"},
#     {"name":"PowerBI Differentiators Demo","url":"https://regale.cloud/Microsoft/viewer/2360/microsoft-fabric-end-to-end-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric end-to-end demo","url":"https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
#     {"name":"Modern Analytics with Microsoft Fabric and Azure Databricks DREAM Lab","url":"https://regale.cloud/Microsoft/viewer/2637/modern-analytics-with-microsoft-fabric-and-azure-databricks-dream-lab/index.html#/0/0"},
#     {"name":"Modern Analytics with Azure Databricks and Power BI DREAM Demo (Partners)","url":"https://regale.cloud/Microsoft/viewer/2426/partners-modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
#     {"name":"Modern Analytics with Azure Databricks and Power BI DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2421/modern-analytics-with-azure-databricks-and-power-bi-dream-demo/index.html#/0/0"},
#     {"name":"CosmosDB + OpenAI DREAM Demo","url":"https://regale.cloud/Microsoft/viewer/2493/cosmosdb-openai-dream-demo/index.html#/0/0"},
#     {"name":"Azure OpenAI Service Dream demo with shopping co-pilot.","url":"https://regale.cloud/Microsoft/viewer/2486/azure-openai-service-dream-demo-with-shopping-co-pilot/index.html#/0/0"},
#     {"name":"Azure OpenAI Service Dream Demo 10-minute","url":"https://regale.cloud/Microsoft/viewer/2383/azure-openai-service-dream-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric Dream Demo (10 minute)","url":"https://regale.cloud/Microsoft/viewer/2466/microsoft-fabric-dream-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric Dream Demo (5 minute)","url":"https://regale.cloud/Microsoft/viewer/2411/microsoft-fabric-dream-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric DREAM Demo (4 Minute) PARTNERS","url":"https://regale.cloud/Microsoft/viewer/2427/partners-microsoft-fabric-dream-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric DREAM Demo (4 Minute)","url":"https://regale.cloud/Microsoft/viewer/2379/microsoft-fabric-dream-demo/index.html#/0/0"},
#     {"name":"Azure OpenAI Service Dream Demo (with admin tool) 10-minute","url":"https://regale.cloud/Microsoft/viewer/2376/azure-openai-service-dream-demo-with-admin-tool/index.html#/0/0"},
#     {"name":"Microsoft Fabric Embedded Demo","url":"https://regale.cloud/Microsoft/viewer/2262/microsoft-fabric-embedded-demo/index.html#/0/0"},
#     {"name":"Microsoft Fabric and Azure Databricks DREAM Demo","url":"https://simdemo.azureedge.net/dai/fabric-databricks/index.html#/0/0"},
#     {"name":"Microsoft Fabric and Azure Databricks DREAM Demo (Partners)","url":"https://regale.cloud/Microsoft/viewer/2428/partners-microsoft-fabric-and-azure-databricks-dream-demo/index.html#/0/0"},
#     {"name":"Azure Databricks and Microsoft Fabric DREAM Demo (booth)","url":"https://regale.cloud/Microsoft/viewer/2303/azure-databricks-and-microsoft-fabric-dream-demo-booth/index.html#/0/0"},
#     {"name":"Power BI Differentiators Dream Demo Full Click by Click","url":"https://regale.cloud/Microsoft/viewer/instance/2053/6338/index.html#/0/0"},
#     {"name":"Analytics in MIDP Dream Demo for BDMs","url":"https://regale.cloud/Microsoft/viewer/2006/analytics-in-midp-dream-demo-for-bdms/index.html#/0/0"},
#     {"name":"Power BI Differentiators Dream Demo Full Click by Click V2","url":"https://regale.cloud/Microsoft/viewer/1947/power-bi-differentiators-dream-demo-integrated-into-web-app/index.html#/0/0"}


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
