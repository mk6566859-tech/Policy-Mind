# PolicyMind — HR Policy Assistant

A polished RAG-based HR Policy Assistant built with:

- Streamlit
- PyMuPDF
- Sentence Transformers
- FAISS
- Groq API

## Architecture

PDF
→ PyMuPDF
→ page-aware text extraction
→ chunking
→ Sentence Transformers embeddings
→ FAISS similarity search
→ relevant policy chunks
→ Groq LLM
→ grounded answer + sources

## Project structure

```text
hr-policy-assistant/
├── app.py
├── services/
│   ├── embeddings.py
│   ├── groq_client.py
│   ├── pdf_processor.py
│   ├── rag_pipeline.py
│   ├── text_splitter.py
│   └── vector_store.py
├── ui/
│   ├── components.py
│   └── styles.py
├── utils/
├── assets/
│   └── logo.png
├── data/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Run locally

### 1. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Groq

Copy `.env.example` to `.env` and add your API key.

Then add this near the top of `app.py` if you want local `.env` loading:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Start Streamlit

```bash
streamlit run app.py
```

## GitHub safety

Never commit:

```text
.env
.streamlit/secrets.toml
```

Your API key belongs in Streamlit Secrets when deployed.

## Streamlit deployment

1. Push this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository.
5. Main file: `app.py`.
6. Add a secret:

```toml
GROQ_API_KEY = "your_real_key"
GROQ_MODEL = "llama-3.3-70b-versatile"
```

7. Deploy.

The code reads environment variables, and Streamlit exposes its secrets to the application environment.

## Notes

- This version handles text-based PDFs.
- Scanned/image-only PDFs need OCR.
- FAISS is built in memory after each upload; this keeps the first version simple and deployment-friendly.
- For a multi-user production system, add persistent storage, authentication, document IDs, and per-user indexes.
