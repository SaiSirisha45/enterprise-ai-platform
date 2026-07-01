import time
import os

from backend.rag.embedding_service import EmbeddingService
from backend.rag.vector_store import search_documents


TEST_QUERIES = [
    {
        "query": "How can I apply for leave?",
        "department": "hr_docs",
        "expected_keyword": "leave"
    },
    {
        "query": "What is payroll process?",
        "department": "payroll_docs",
        "expected_keyword": "payroll"
    }
]


CHUNK_SIZES = [500, 750, 1000]
CHUNK_OVERLAPS = [50, 100, 200]

EMBEDDING_MODELS = [
    "sentence-transformers/all-MiniLM-L6-v2"
]


def evaluate_model(model_name: str):
    service = EmbeddingService(model_name=model_name)
    results = []

    for chunk_size in CHUNK_SIZES:
        for overlap in CHUNK_OVERLAPS:
            for test in TEST_QUERIES:
                start = time.time()

                embedding = service.generate_embedding(test["query"])

                search_result = search_documents(
                    department=test["department"],
                    query_embedding=embedding["vector"],
                    top_k=3
                )

                latency = time.time() - start

                documents = search_result.get("documents", [[]])[0]

                accuracy = 0

                for doc in documents:
                    if test["expected_keyword"].lower() in doc.lower():
                        accuracy = 1
                        break

                results.append({
                    "model": model_name,
                    "chunk_size": chunk_size,
                    "overlap": overlap,
                    "query": test["query"],
                    "latency": round(latency, 4),
                    "top_k_accuracy": accuracy
                })

    return results


def generate_report(results):
    report = "# Retrieval Benchmark Report\n\n"

    report += "## Evaluation Metrics\n\n"
    report += "- Embedding Models\n"
    report += "- Chunk Sizes\n"
    report += "- Chunk Overlap\n"
    report += "- Vector Search Latency\n"
    report += "- Top-K Accuracy\n\n"

    report += "| Model | Chunk Size | Overlap | Query | Latency | Top-K Accuracy |\n"
    report += "|---|---:|---:|---|---:|---:|\n"

    for r in results:
        report += (
            f"| {r['model']} | {r['chunk_size']} | {r['overlap']} | "
            f"{r['query']} | {r['latency']}s | {r['top_k_accuracy']} |\n"
        )

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    report_dir = os.path.join(base_dir, "evaluation")
    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(report_dir, "retrieval_report.md")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("Benchmark completed.")
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    all_results = []

    for model in EMBEDDING_MODELS:
        all_results.extend(evaluate_model(model))

    generate_report(all_results)