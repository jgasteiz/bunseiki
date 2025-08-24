import pydantic_ai


agent = pydantic_ai.Agent(
    model="openai:gpt-4.1",
    output_type=str,
    instructions=(
        "You're a sentence generator for practicing Japanese."
        "You will be given a word in Japanese, and you need to create a sentence using that word."
        "The sentence should not be too simple or too complex."
        "The point is for the user to have a good example of the word in context."
    ),
)


def generate_sentence(
    word: str,
) -> str:
    """
    Generate a list of drills using AI.
    """
    result = agent.run_sync(
        user_prompt=word,
    )
    return result.output
