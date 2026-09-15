import numpy as np

from services.pdf_processor import extract_pages
from services.text_splitter import build_chunks
from services.embeddings import embed_texts, get_embedding_model
from services.vector_store import VectorStore
from services.groq_client import generate_answer


class RAGPipeline:
    def __init__(self):
        self.vector_store = VectorStore()
        self.document_name = None
        self.stats = None

    def ingest_pdf(self, uploaded_file) -> dict:
        pdf_bytes = uploaded_file.getvalue()
        pages = extract_pages(pdf_bytes)

        chunks = build_chunks(
            pages,
            chunk_size=900,
            overlap=150,
        )

        if not chunks:
            raise ValueError("The PDF did not produce any usable text chunks.")

        texts = [item["text"] for item in chunks]
        embeddings = embed_texts(texts)

        self.vector_store.build(embeddings, chunks)
        self.document_name = uploaded_file.name

        dimension = int(np.asarray(embeddings).shape[1])

        self.stats = {
            "pages": len(pages),
            "chunks": len(chunks),
            "embedding_dimension": dimension,
            "model": "all-MiniLM-L6-v2",
        }

        return self.stats

    def ask(self, question: str, top_k: int = 5):
        model = get_embedding_model()
        query_embedding = model.encode(
            [question],
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        results = self.vector_store.search(query_embedding, top_k=top_k)

        if not results:
            return (
                "I couldn't find relevant information in the uploaded policy.",
                [],
            )

        # A similarity threshold helps avoid confidently answering from unrelated chunks.
        relevant = [item for item in results if item["score"] >= 0.25]

        if not relevant:
            return (
                "I couldn't find enough relevant information in the uploaded policy "
                "to answer that question.",
                [],
            )

        context_parts = []
        sources = []

        for number, item in enumerate(relevant, start=1):
            context_parts.append(
                f"[Source {number} | Page {item['page']}]\n{item['text']}"
            )
            sources.append(
                {
                    "page": item["page"],
                    "score": round(item["score"], 3),
                    "text": item["text"],
                }
            )

        context = "\n\n".join(context_parts)
        answer = generate_answer(question, context)

        return answer, sources

    def clear(self):
        self.vector_store.clear()
        self.document_name = None
        self.stats = None
