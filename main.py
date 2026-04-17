import os
from dotenv import load_dotenv
from src.ingestion.scraper import fetch_rbi_press_releases
from src.ingestion.content_processor import scrape_content, chunk_text
from src.ingestion.vector_store import initialize_db, add_to_vault

# Load environment variables
load_dotenv()

def run_pipeline():
    print("--- Starting Regulatory Alpha Ingestion Pipeline ---")
    
    # 1. Initialize the Vector Database
    vault = initialize_db()
    
    # 2. Scrape the latest links
    releases = fetch_rbi_press_releases()
    
    if not releases:
        print("No releases found. Pipeline stopped.")
        return

    # 3. Process the top 3 releases (Starting small for testing)
    # This demonstrates "Iterative Development" - a key PM trait.
    for item in releases[:3]:
        print(f"\nProcessing: {item['title']}")
        
        # Extract the prid from the URL for a unique ID
        prid = item['link'].split('prid=')[-1]
        
        # Get the full text
        full_text = scrape_content(item['link'])
        
        if full_text:
            # Break text into chunks for the AI to handle
            chunks = chunk_text(full_text)
            
            # Save to the Vector Vault with Metadata
            # Metadata is crucial for "Decision-support systems" [cite: 22]
            metadata = {
                "title": item['title'],
                "link": item['link'],
                "prid": prid,
                "source": "RBI"
            }
            
            add_to_vault(vault, chunks, metadata)
        else:
            print(f"Skipping {prid} due to empty content.")

    print("\n--- Pipeline Completed Successfully ---")

if __name__ == "__main__":
    run_pipeline()