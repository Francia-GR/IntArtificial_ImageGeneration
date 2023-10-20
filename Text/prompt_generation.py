import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model = "gpt-3.5",
    prompts = "Text",
    temperature = 0.7,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
)

print(response["choices"][0]["text"])