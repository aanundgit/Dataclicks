import streamlit as st
import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import date

st.set_page_config(page_title="RSS Feed", layout="wide")
st.markdown(
    """
    <style>
    .custom-title {
        color: #31333F;  /* Saffron yellow color */
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title with custom styling
st.markdown('<p class="custom-title">Latest Product Updates </p>', unsafe_allow_html=True)
st.write("Current Date:", date.today()) 
st.markdown("""<hr style="height:2px;border:none;color:#F4C430;background-color:#F4C430;" /> """,
            unsafe_allow_html=True)
 


# List of RSS feeds
RSS_FEEDS = {
    "Fabric Blog": "https://blog.fabric.microsoft.com/en-us/blog/feed/",
    "Power BI Blog": "https://fetchrss.com/rss/66c5224e42f425d7c206218266c522269f4b9c68810d6db2.atom",
    "Azure Updates" : "https://fetchrss.com/rss/66c5224e42f425d7c206218266c524209e0dc71d0e03cfd3.xml",
}

# Function to fetch and parse RSS feed using requests
def fetch_rss_feed(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            st.error(f"Failed to retrieve feed: HTTP {response.status_code}")
            return None

        content_type = response.headers.get('Content-Type', '').lower()

        # If the content type is XML or contains 'rss', directly parse it
        if 'xml' in content_type or 'rss' in content_type:
            return feedparser.parse(response.content)

        # Attempt to parse as HTML and find a linked RSS feed
        soup = BeautifulSoup(response.content, 'html.parser')
        rss_link = soup.find('link', type='application/rss+xml')
        if rss_link and rss_link['href']:
            rss_feed_url = rss_link['href']
            if not rss_feed_url.startswith('http'):
                rss_feed_url = requests.compat.urljoin(url, rss_feed_url)
            return feedparser.parse(rss_feed_url)
        
        # Manual scraping fallback (non-standard feeds)
        articles = soup.find_all('article')
        if articles:
            entries = []
            for article in articles:
                title = article.find('h2').text if article.find('h2') else 'No Title'
                link = article.find('a')['href'] if article.find('a') else '#'
                published = article.find('time')['datetime'] if article.find('time') else ''
                summary = article.find('p').text if article.find('p') else 'No Summary'
                
                entries.append({
                    'title': title,
                    'link': link,
                    'published': published,
                    'summary': summary
                })
            return {'feed': {'title': 'Manually Scraped Feed', 'link': url}, 'entries': entries}

        # If none of the above works, return None
        st.error("Unable to parse the RSS feed. The format may not be supported.")
        return None

    except Exception as e:
        st.error(f"An error occurred while fetching the feed: {e}")
        return None

# Function to format date
def format_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%b %d, %Y')
    except Exception as e:
        return "Unknown Date"

# Function to display RSS feed entries as cards
def display_feed(feed):
    if feed is None or not feed.get('entries'):
        st.error("Failed to parse the RSS feed. The feed might be in an unsupported format or inaccessible.")
        return

    st.write(f"## {feed['feed'].get('title', 'RSS Feed')}")
    
    # Card layout styling
    st.markdown(
        """
        <style>
        .card {
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 20px;
            background-color: #f5f5f5;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .card h3 {
            margin: 0 0 10px 0;
            font-size: 18px;
            font-weight: bold;
        }
        .card p {
            margin: 0 0 10px 0;
            font-size: 14px;
        }
        .card a {
            color: #333;
            text-decoration: none;
        }
        .card a:hover {
            text-decoration: underline;
        }
        .card .date {
            font-size: 12px;
            color: #6c757d;
            margin-bottom: 10px;
        }
        @media screen and (max-width: 768px) {
            .card {
                padding: 12px;
            }
            .card h3 {
                font-size: 16px;
            }
            .card p {
                font-size: 12px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display entries as cards
    for entry in feed['entries']:
        st.markdown(
            f"""
            <div class="card">
                <a href="{entry['link']}">
                    <h3>{entry['title']}</h3>
                </a>
                <div class="date">{format_date(entry.get('published', ''))}</div>
                <p>{entry['summary']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Main App

#st.title("Latest Updates")
st.markdown("##### Select a feed to stay updated with the latest news")

# Dropdown for RSS Feed selection
selected_feed = st.selectbox("Select RSS Feed", list(RSS_FEEDS.keys()))

# Fetch and display the selected feed
if selected_feed:
    feed_url = RSS_FEEDS[selected_feed]
    feed = fetch_rss_feed(feed_url)
    if feed:
        display_feed(feed)

# Custom CSS for improved aesthetics and responsiveness
st.markdown(
    """
    <style>
    .stContainer { padding: 16px; }
    .stTextInput { margin-bottom: 24px; }
    .stTextInput > label { font-size: 18px; font-weight: 500; color: #333333; }
    .stTextInput > div > input { font-size: 16px; padding: 8px; }
    </style>
    """,
    unsafe_allow_html=True,
)