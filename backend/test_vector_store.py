from rag.embedding_service import EmbeddingService
from rag.vector_store import insert_document, search_documents

service = EmbeddingService()

text = "HR leave policy allows employees to apply for annual leave."

embedding = service.generate_embedding(text)

insert_result = insert_document(
    department="hr_docs",
    document_id="doc_1",
    chunk_id="chunk_1",
    chunk_text=text,
    embedding=embedding["vector"],
    metadata={
        "department": "HR",
        "owner": "Admin",
        "status": "Approved"
    }
)

print(insert_result)

query_embedding = service.generate_embedding("How can I apply for leave?")

search_result = search_documents(
    department="hr_docs",
    query_embedding=query_embedding["vector"],
    top_k=3
)

print(search_result)