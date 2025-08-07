# Multi-LLM Chat Agent with Chainlit and OpenAI SDK

This is a multi-LLM chat assistant powered by Chainlit and OpenAI SDK. It allows you to switch between several language models like Gemini, Deepseek, Qwen, and MoonshotAI on the fly using a simple dropdown menu in the chat UI.

# 🌟 Chainlit Multi-LLM Chat Assistant

This project is a **Chainlit-powered AI assistant** that allows users to interact with multiple Large Language Models (LLMs) via a dynamic chat interface. Users can select from a variety of models like Qwen, DeepSeek, Gemini, and MoonshotAI, and receive streamed responses in real-time.

---
   
## 🚀 Features

- 🔄 **Dynamic Model Switching** — Choose from multiple LLMs during the chat session.
- 💬 **Streamed Responses** — Real-time streaming of model replies for smoother UX.
- 🔐 **Secure API Integration** — Uses environment variables to manage API keys and base URLs.
- 🧠 **Agent Architecture** — Modular agent setup for flexible instruction and model handling.
- 🛠️ **Chainlit Widgets** — Interactive UI elements for model selection and chat control.
       
---

## 🧰 Technologies Used

| Tool/Library       | Purpose                                  |
|--------------------|------------------------------------------|
| `Chainlit`         | Chat interface and widget handling       |
| `OpenAI` SDK       | Async client for external LLMs           |
| `dotenv`           | Environment variable management          |
| `Custom Agent`     | Modular agent and runner logic           |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/chainlit-multi-llm-chat.git
   cd chainlit-multi-llm-chat

2. **Clone the repository**
   ```bash
   pip install -r requirements.txt
3. **Set up environment variables**
   Create a .env file in the root directory:
    ```Env
    OPENROUTER_API_KEY=your_openrouter_api_key
    base_url=https://openrouter.ai/api/v1
##🧪 Running the App
Start the Chainlit server:
    ```bash
    chainlit run main.py


 ##🧠 Supported Models
* Qwen 3
* Deepseek v3
* Gemini 2.0
* DeepSeek R1
* MoonshotAI k
##🙌 Credits
Developed by Kaif Shamim Powered by Chainlit and OpenRouter



