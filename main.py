import os  
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent
from openai import AsyncOpenAI

from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import chainlit as cl

# Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# API keys and base url for external LLMs
gemini_api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("base_url")

history = []

# Updated models dictionary with your new model names and IDs
models = {
    "Qwen 3": "qwen/qwen3-coder:free",
    "Deepseek v3": "deepseek/deepseek-chat-v3-0324:free",
    "gemini 2.0": "google/gemini-2.0-flash-exp:free",
    "DeepSeek R1": "deepseek/deepseek-r1-0528:free",
    "MoonshotAI k2": "moonshotai/kimi-k2:free"
}

@cl.on_chat_start
async def handle_start_chat():
    await cl.Message(content="Hello, how can I help you today?").send()

    # Send chat settings widget for model selection
    await cl.ChatSettings(
        [
            cl.input_widget.Select(
                id="Model",
                label="Choose Any LLM Model",
                items={k: k for k in models.keys()},  # dict of key->label
                value=list(models.keys())[0],         # default selected model key as string
            )
        ]
    ).send()

    # Initialize selected model in user session
    cl.user_session.set("model", list(models.keys())[0])

@cl.on_message
async def handle_message(message: cl.Message):
    # Handle model selection widget event
    if message.type == "widget" and message.id == "Model":
        selected_model_key = message.value
        if selected_model_key in models:
            cl.user_session.set("model", selected_model_key)
            await cl.Message(content=f"Model updated to {selected_model_key}").send()
        else:
            await cl.Message(content=f"Unknown model selected: {selected_model_key}").send()
        return  # Do NOT process this message further

    # Normal user message processing

    user_input = message.content
    history.append({"role": "user", "content": user_input})

    # Retrieve selected model from session
    selected_model_key = cl.user_session.get("model", list(models.keys())[0])
    selected_model = models[selected_model_key]

    # Setup OpenAI Async Client with your external LLM credentials
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url=base_url
    )

    # Create your model wrapper
    model = OpenAIChatCompletionsModel(
        model=selected_model,
        openai_client=external_client
    )

    # Instantiate your agent
    agent = Agent(
        name="Kaif Shamim",
        instructions="You are a helpful assistant.",
        model=model
    )

    # Run the agent with streamed output
    response = Runner.run_streamed(agent, input=user_input)

    # Prepare Chainlit message for streaming response
    stream_response = cl.Message(content="")
    await stream_response.send()

    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            stream_response.content += event.data.delta
            await stream_response.update()
