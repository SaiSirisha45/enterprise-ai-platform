class RAGOptimizer:


    def __init__(self):

        self.results = []



    def benchmark(
        self,
        chunk_size,
        overlap,
        embedding_model,
        top_k,
        latency,
        accuracy,
        tokens,
        cost
    ):


        result = {

            "chunk_size":
            chunk_size,

            "overlap":
            overlap,

            "embedding_model":
            embedding_model,

            "top_k":
            top_k,

            "latency_ms":
            latency,

            "accuracy":
            accuracy,

            "token_usage":
            tokens,

            "cost":
            cost

        }


        self.results.append(result)

        return result



    def best_configuration(self):

        if not self.results:
            return None


        return sorted(
            self.results,
            key=lambda x:
            (
                -x["accuracy"],
                x["latency_ms"],
                x["cost"]
            )
        )[0]



rag_optimizer = RAGOptimizer() 
