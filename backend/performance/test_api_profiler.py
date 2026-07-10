from backend.performance.api_profiler import profiler



@profiler.profile(
    "chat_api"
)
def chat():

    return "AI Response"



print(
    chat()
)


print(
    profiler.get_report()
) 