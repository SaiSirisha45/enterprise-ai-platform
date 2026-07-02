from rag.document_processor import process_document

result = process_document(
    "../storage/documents/tool_catalog.md",
    chunk_size=500,
    overlap=50
)

print(result["metadata"])
print("Total Chunks:", result["total_chunks"])
print(result["chunks"][0])