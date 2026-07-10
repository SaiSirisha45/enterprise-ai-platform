import os
import re
from pypdf import PdfReader
from docx import Document
from bs4 import BeautifulSoup


def extract_text(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() or "" for page in reader.pages])

    if ext == ".docx":
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    if ext in [".txt", ".md", ".markdown"]:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    if ext == ".html":
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            return soup.get_text(separator="\n")

    raise ValueError("Unsupported file type")


def clean_text(text: str):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50):
    chunks = []
    start = 0
    chunk_number = 1

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append({
            "chunk_number": chunk_number,
            "chunk_text": chunk_text
        })

        chunk_number += 1
        start += chunk_size - overlap

    return chunks


def extract_metadata(file_path: str):
    return {
        "file_name": os.path.basename(file_path),
        "document_type": os.path.splitext(file_path)[1].replace(".", ""),
        "file_path": file_path
    }


def process_document(file_path: str, chunk_size: int = 500, overlap: int = 50):
    raw_text = extract_text(file_path)
    cleaned_text = clean_text(raw_text)
    chunks = split_into_chunks(cleaned_text, chunk_size, overlap)
    metadata = extract_metadata(file_path)

    return {
        "metadata": metadata,
        "chunk_size": chunk_size,
        "overlap": overlap,
        "total_chunks": len(chunks),
        "chunks": chunks
    }