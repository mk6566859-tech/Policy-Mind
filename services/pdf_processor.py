import fitz


def extract_pages(pdf_bytes: bytes) -> list[dict]:
    """Extract text page-by-page while preserving page numbers."""
    pages = []

    with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()
            if text:
                pages.append(
                    {
                        "page": page_number,
                        "text": text,
                    }
                )

    if not pages:
        raise ValueError(
            "No readable text was found in this PDF. "
            "If it is a scanned document, OCR is required."
        )

    return pages
