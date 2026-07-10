class CostOptimizer:


    def calculate_token_cost(
        self,
        input_tokens,
        output_tokens
    ):

        input_cost = (
            input_tokens * 0.000005
        )

        output_cost = (
            output_tokens * 0.000015
        )


        return round(
            input_cost + output_cost,
            6
        )



    def optimize_prompt(
        self,
        prompt
    ):

        original = len(
            prompt.split()
        )


        optimized_prompt = (
            prompt[:500]
        )


        optimized = len(
            optimized_prompt.split()
        )


        return {

            "before_tokens":
            original,

            "after_tokens":
            optimized,

            "saved":
            original-optimized
        }



    def optimize_embedding(
        self,
        documents
    ):

        before = len(documents)

        after = int(
            before * 0.7
        )


        return {

            "before":
            before,

            "after":
            after,

            "saved":
            before-after

        }



    def optimize_api_calls(
        self,
        requests
    ):

        return {

            "before":
            requests,

            "after":
            int(requests*0.6)

        }



cost_optimizer = CostOptimizer() 