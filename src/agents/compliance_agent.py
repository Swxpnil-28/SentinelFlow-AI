import os
from openai import OpenAI
from dotenv import load_dotenv
from src.ingestion.vector_store import initialize_db

load_dotenv()

# Pointing to Groq's high-speed infrastructure
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def query_regulatory_knowledge(question):
    vault = initialize_db()
    
    # RAG: Retrieve context from your Vector Vault
    results = vault.query(
        query_texts=[question],
        n_results=3
    )
    
    context = "\n".join(results['documents'][0])
    
    # System prompt [cite: 6]
    system_prompt = """
### ROLE
You are the SentinelFlow Intelligence Agent. You are an expert in financial regulations (RBI/SEBI) and provide high-leverage strategic analysis for executive leadership.

### MANDATE
- Provide structured, blunt, and actionable analysis.
- Use ONLY the provided context. 
- If the context is missing info, state: "SentinelFlow Vault does not currently contain data on [Topic]."

### STRICT CONSTRAINTS
1. CHARACTER: Remain a professional Regulatory Strategist. No recipes, jokes, or non-financial advice.
2. SCOPE: Restrict analysis to Finance, Risk, Legal, or Operations. 
3. HALLUCINATION: Cite specific document titles for every fact. No invented yields or dates.

### OUTPUT FORMAT
- STRATEGIC SUMMARY
- RISK EXPOSURE ANALYSIS
- OPERATIONAL NEXT STEPS
"""
   # 4. Generate the response using a 2026-supported model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context for Analysis:\n{context}\n\nQuestion: {question}"}
        ],
        temperature=0.0  # Ensures deterministic, non-hallucinated results
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    user_query = "What is the redemption price for the Sovereign Gold Bond 2020-21 Series VII?"
    print(f"QUERYING VAULT: {user_query}\n")
    print(query_regulatory_knowledge(user_query))