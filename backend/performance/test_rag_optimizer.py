from backend.performance.rag_optimizer import rag_optimizer


rag_optimizer.benchmark(
    500,
    50,
    "text-embedding-model",
    5,
    200,
    0.92,
    1200,
    0.03
)


rag_optimizer.benchmark(
    1000,
    100,
    "text-embedding-model",
    10,
    400,
    0.95,
    2000,
    0.06
)


print(
    rag_optimizer.best_configuration()
) 