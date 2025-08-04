Getting Started
Prerequisites
Python 3.8+

Chainlit installed (pip install chainlit)

OpenAI Python SDK (pip install openai)

Your .env file with:

env
Copy code
OPENROUTER_API_KEY=your_api_key_here
base_url=https://your-llm-endpoint.com
Installation
Clone the repo:

bash
Copy code
git clone https://github.com/yourusername/multi-llm-chainlit.git
cd multi-llm-chainlit
Create and activate a virtual environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your API keys and base URL to .env file.

Usage
Run the Chainlit app with:

bash
Copy code
chainlit run your_script.py
Replace your_script.py with the main Python file containing the code.

Open the UI at http://localhost:8000 (default).

You can select the desired LLM model from the dropdown at the start or anytime during the chat. The assistant will respond using the selected model.

Code Overview
@cl.on_chat_start: Sends a greeting message and presents the model selection dropdown.

@cl.on_message: Handles user messages and widget events (model selection changes).

Stores selected model in the user session.

Streams responses from the selected model back to the UI.



Acknowledgments
Chainlit

OpenAI SDK

Model providers like Gemini, Deepseek, Qwen, MoonshotAI