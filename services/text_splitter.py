import re


def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_text(text: str, chunk_size: int = 900, overlap: int = 150) -> list[str]:
    """
    Character-based chunker designed to be simple and predictable.
    Chunks are created without splitting a word where possible.
    """
    text = normalize_text(text)

    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)

        if end < text_length:
            boundary = text.rfind(" ", start, end)
            if boundary > start + int(chunk_size * 0.65):
                end = boundary

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start = max(0, end - overlap)

    return chunks


def build_chunks(pages: list[dict], chunk_size: int = 900, overlap: int = 150) -> list[dict]:
    chunks = []

    for page in pages:
        for chunk in split_text(page["text"], chunk_size, overlap):
            chunks.append(
                {
                    "text": chunk,
                    "page": page["page"],
                }
            )

    return chunks
