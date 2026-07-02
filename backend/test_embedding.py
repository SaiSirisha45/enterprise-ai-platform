from rag.embedding_service import EmbeddingService

service = EmbeddingService()

result = service.generate_embedding("This is a test company document.")

print("Embedding ID:", result["embedding_id"])
print("Model:", result["model_used"])
print("Dimension:", result["vector_dimension"])
print("Processing Time:", result["processing_time"])
print("First 5 values:", result["vector"][:5])