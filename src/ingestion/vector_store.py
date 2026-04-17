import chromadb
from chromadb.utils import embedding_functions

# Use a local embedding model (no API key needed, very 'Engineer' style)
default_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def initialize_db():
    # This creates a folder called 'rbi_vault' where your data is stored permanently
    client = chromadb.PersistentClient(path="./data/rbi_vault")
    
    # Create or get the collection (think of this as a table)
    collection = client.get_or_create_collection(
        name="regulatory_updates",
        embedding_function=default_ef
    )
    return collection

def add_to_vault(collection, chunks, metadata):
    """Stores the text chunks in the database."""
    ids = [f"{metadata['prid']}_{i}" for i in range(len(chunks))]
    metadatas = [metadata for _ in chunks]
    
    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=metadatas
    )
    print(f"Successfully added {len(chunks)} chunks to the vault.")