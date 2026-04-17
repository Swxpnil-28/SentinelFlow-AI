#  SentinelFlow AI
### *Regulatory Intelligence & Automated Compliance Engine*

*SentinelFlow AI* is a high-leverage RAG (Retrieval-Augmented Generation) system architected to navigate the "non-linear chaos" of financial regulation. Built specifically for the Indian banking landscape, it automates the ingestion of RBI press releases and transforms fragmented policy updates into a searchable, high-fidelity knowledge vault.

In a sector where precision is the only currency, SentinelFlow provides a "Quiet Luxury" solution: minimal, mathematically rigorous, and incredibly fast.

---

##  The Architecture

The engine is built on a "Privacy-First, Performance-Always" framework. By handling heavy vectorization locally and offloading inference to high-speed hardware, we ensure compliance data stays secure while response times remain sub-second.

* *Inference Layer:* Powered by *Groq LPU Acceleration* for near-instant, human-speed dialogue.
* *Vector Database:* Utilizes *ChromaDB* for persistent, semantic storage of regulatory "memory."
* *Local Embeddings:* Runs the *all-MiniLM-L6-v2* transformer model on-device. This ensures that sensitive regulatory text is vectorized without external API exposure, maintaining a higher standard of data privacy.
* *Ingestion Pipeline:* A custom scraper designed for the RBI interface that handles semantic boundary detection and intelligent chunking.

---

##  Engine Capabilities

* *Automated Policy Scraping:* Real-time ingestion of official RBI announcements, moving from raw HTML/PDF to structured vector data.
* *Semantic Risk Analysis:* Context-aware querying (e.g., "What is the impact on prepaid payment instruments?") that finds meaning, not just keywords.
* *Low-Latency RAG:* Optimized for environments where time-to-insight is a critical metric.
* *Repository Hygiene:* A production-ready codebase following modular engineering standards and sanitization protocols.

---

##  Quick Start Guide

### *1. Preparation*
* Python 3.10+ installed.
* A *Groq API Key* (obtainable at [console.groq.com](https://console.groq.com)).

### *2. Installation*
```bash
# Clone the repository
git clone [https://github.com/Swxpnil-28/SentinelFlow-AI.git](https://github.com/Swxpnil-28/SentinelFlow-AI.git)
cd SentinelFlow-AI

# Create and activate a clean environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac

# Install specialized dependencies
pip install -r requirements.txt
```
### *3. Environment Config*
```bash
Create a .env file in the root directory to store your credentials securely:
GROQ_API_KEY=your_actual_groq_api_key_here
```
### *4. System Launch*
```bash
set PYTHONPATH=. && streamlit run src/app/dashboard.py
```
---
## Project Structure
``` bash
SentinelFlow-AI/
├── src/
│   ├── agents/         # Intelligence orchestration & compliance logic
│   ├── ingestion/      # Scrapers, vector store initialization, & processing
│   └── app/            # Streamlit executive dashboard
├── data/               # Persistent 'rbi_vault' (Local Vector Store)
├── requirements.txt    # Sanitized dependency tree
└── README.md           # System documentation
```
---
 ## Engineering Ethos
 
SentinelFlow was built with a specific mindset: Math over convenience. By avoiding bloated generic wrappers and focusing on specialized local embeddings, we reduce model hallucinations and ensure that every compliance insight is grounded in official documentation. It is an engine built for those who value calm, systematic order within complex financial ecosystems.

---
##Disclaimer and License

This system is intended as an assistant for regulatory research and institutional compliance. It does not constitute formal legal advice.

Maintained by [Swapnil-28] — Engineering clarity for the financial sector.
