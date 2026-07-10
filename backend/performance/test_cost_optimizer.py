from backend.performance.cost_optimizer import cost_optimizer


print(
    cost_optimizer.calculate_token_cost(
        10000,
        2000
    )
)


print(
    cost_optimizer.optimize_prompt(
        "This is a very long prompt "
        "with unnecessary information"
    )
)


print(
    cost_optimizer.optimize_embedding(
        [
            "doc1",
            "doc2",
            "doc3",
            "doc4"
        ]
    )
)


print(
    cost_optimizer.optimize_api_calls(
        1000
    )
) 