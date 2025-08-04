# Multi-LLM Chat Agent with Chainlit and OpenAI SDK

This is a multi-LLM chat assistant powered by Chainlit and OpenAI SDK. It allows you to switch between several language models like Gemini, Deepseek, Qwen, and MoonshotAI on the fly using a simple dropdown menu in the chat UI.

---

## 🛠 Getting Started

### ✅ Prerequisites

- Python 3.8+
- [Chainlit](https://chainlit.io)  
  ```bash
  pip install chainlit

### OpenAI Python SDK

 ```bash
pip install openai
### 📄 .env Configuration
Create a .env file in the root directory and add the following:

env
OPENROUTER_API_KEY=your_api_key_here
base_url=https://your-llm-endpoint.com
###📦 Installation
Clone the repository:

 ```bash
git clone https://github.com/yourusername/multi-llm-chainlit.git
cd multi-llm-chainlit
Create and activate a virtual environment:

 ```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
###Install dependencies:

 ```bash

pip install -r requirements.txt
Add your API keys to .env file as shown above.

###🚀 Usage
Run the Chainlit app:

 ```bash
chainlit run your_script.py
Replace your_script.py with the name of your Python script (e.g., app.py or main.py).

Then open your browser to:
📍 http://localhost:8000

