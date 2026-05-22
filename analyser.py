import dataclasses

import pydantic_ai


@dataclasses.dataclass
class Example:
    sentence: str
    translation: str


@dataclasses.dataclass
class AnalysisOutput:
    grammar_point: str
    explanation: str
    examples: list[Example]


agent = pydantic_ai.Agent(
    model="anthropic:claude-haiku-4-5-20251001",
    output_type=AnalysisOutput,
    instructions=(
        "You are a Japanese grammar analyser for language learners."
        " You will be given a Japanese sentence."
        " Identify the single most relevant or most complex grammar point in the sentence."
        " Focus on patterns that would be most useful for a JLPT N3 learner to understand."
        " Provide a concise explanation of the grammar point in English."
        " Give 2-3 short alternative example sentences using the same grammar point,"
        " each with an English translation."
        " Do not give a full grammatical breakdown — focus only on the one key grammar point."
    ),
)


def analyse_sentence(sentence: str) -> AnalysisOutput:
    result = agent.run_sync(user_prompt=sentence)
    return result.output
