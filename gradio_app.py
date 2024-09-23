from openai import OpenAI
import gradio as gr

client = OpenAI(api_key="EMPTY", base_url="http://localhost:10789/v1")
system_prompt = "You are a helpful assistant that answers in the style of early American written sources"


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "system", "content": system_prompt})
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="./models/eam-bot",
        messages=history_openai_format,
        temperature=0.7,
        stream=True,
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message


with open("README.md", "r") as f:
    description = f.read()


gr.ChatInterface(
    predict,
    title="Early American Historichat",
    description=description,
    examples=[
        "Why is the sky blue?",
        "Why is water wet?",
        "Why did Judas rat to Romans while Jesus slept?",
    ],
).queue().launch(show_api=False)
