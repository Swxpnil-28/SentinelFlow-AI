import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter

def scrape_content(url):
    """Visits the RBI link and pulls the actual text of the regulation."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # RBI content is usually inside a table or specific div
        # We'll grab all text for now and clean it
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return ""

def chunk_text(text):
    """Breaks long regulations into bite-sized pieces for the AI."""
    # A 'System Thinking' move: LLMs have a limit on how much they can read at once.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    return splitter.split_text(text)