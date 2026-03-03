### LangGraph Agentic AI Application

Stateful AI Workflows using LangGraph + Streamlit + Groq LLM

This project is a Stateful Agentic AI system built using:

🧠 LangGraph (AI workflow orchestration)

🤖 Groq LLM (LLaMA Models)

🌐 Tavily Web Search API

🎨 Streamlit UI

⚡ Python

It supports three intelligent use cases:

🗣️ Basic Chatbot

🌍 Chatbot with Web Search

📰 AI News Summarizer

📌 What This Project Demonstrates

✅ Stateful AI Agents
✅ Tool Integration with LLM
✅ Conditional Graph Routing
✅ Multi-Step AI Pipelines
✅ Real-Time Web Search Integration
✅ News Fetch → Summarize → Save Workflow
✅ Clean Modular Architecture

🏗️ Complete Architecture Overview
🔹 High Level Flow
4
📂 Project Structure

app.py
src/
├── LanggraphAgenticAI/
│ ├── main.py
│ ├── Graph/
│ │ └── graph_builder.py
│ ├── Nodes/
│ │ ├── basic_chatbot_node.py
│ │ ├── chatbot_with_tool_node.py
│ │ └── ai_news_node.py
│ ├── Tools/
│ │ └── search_tool.py
│ ├── state/
│ │ └── state.py
│ ├── LLMS/
│ │ └── groqllm.py
│ └── UI/
│ ├── uiconfigfile.ini
│ ├── uiconfigfile.py
│ └── StreamlitUI/
│ ├── loadui.py
│ └── display_result.py
🧠 How The Application Works (Simple Explanation)

Let’s explain step by step so even beginners understand 👇

1️⃣ app.py – Entry Point
from src.LanggraphAgenticAI.main import load_langgraph_agenticai_app

This file only does one thing:

It calls:

load_langgraph_agenticai_app()

So basically:

👉 When you run the app, it loads the Streamlit AI application.

2️⃣ main.py – The Brain Controller

This is the central controller of the app.

It performs:

Loads UI

Gets user input

Configures LLM

Builds LangGraph

Executes selected workflow

Displays result

Simple Flow:
Load UI
↓
Get User Input
↓
Select Use Case
↓
Load LLM Model
↓
Build Graph
↓
Run Graph
↓
Show Output
3️⃣ UI Layer (Streamlit)
🔹 loadui.py

This builds the entire sidebar UI.

It:

Loads model options

Loads use case options

Takes API keys

Takes user input

Handles AI News frequency selection

Everything user selects is stored in:

self.user_controls
🔹 uiconfigfile.ini

This is configuration file.

It stores:

Page title

LLM options

Model options

Use cases

So instead of hardcoding values, we read from config file.

Very professional design practice ✅

4️⃣ LLM Layer (groqllm.py)

This connects to Groq API.

ChatGroq(api_key=groq_api_key, model=selected_groq_model)

User selects:

Model

API Key

And we create LLM object dynamically.

5️⃣ LangGraph – Core Intelligence

Now comes the most important part 🚀

LangGraph lets us create Stateful AI Workflows

All workflows use this shared state:

class State(TypedDict):
messages: Annotated[list, add_messages]

State stores conversation messages.

🔹 Use Case 1: Basic Chatbot
Graph Flow:
START
↓
Chatbot Node
↓
END
Node Used:

BasicChatbotNode

This simply sends messages to LLM and returns response.

Very simple.

🔹 Use Case 2: Chatbot with Web

Now it becomes more advanced 👇

Graph Flow:
START
↓
Chatbot
↓
(If Tool Needed?)
↓
Tool Node
↓
Back to Chatbot
↓
END
What Happens?

User asks question

LLM decides if tool is required

If required → Tavily search tool runs

Tool result returns to chatbot

LLM generates final answer

This uses:

tools_condition

This enables conditional branching.

This is true agentic AI behavior.

🔹 Use Case 3: AI NEWS

This is a multi-step pipeline.

Graph Flow:
START
↓
Fetch News
↓
Summarize News
↓
Save Result as Markdown
↓
END
Step 1: Fetch News

Using:

TavilyClient()

Fetches latest AI news.

Step 2: Summarize News

LLM:

Formats news

Sorts by date

Generates markdown summary

Step 3: Save Result

Creates file:

./AINews/daily_summary.md

Then UI displays markdown content.

🧠 Why This Project is Powerful

This project demonstrates:

- Stateful Graph Execution

- Multi-Step AI pipelines

- Tool-based LLM agents

- Conditional routing

- External API integration

- Production-level structure

- This is NOT just a chatbot.

This is a Graph-based Agentic AI System.

🚀 Installation
1️⃣ Clone
git clone https://github.com/awasthi-anjali/Agentic-ChatBot.git
cd langgraph-agentic-ai
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set API Keys

You need:

GROQ_API_KEY

TAVILY_API_KEY

You can enter them in the UI.

5️⃣ Run App
streamlit run app.py
🎯 Use Cases
🗣️ Basic Chatbot

Simple conversation with selected Groq model.

🌍 Chatbot with Web

LLM + Tavily Search Tool Integration.

📰 AI News

Fetches latest AI news and generates summarized markdown report.

🔮 Future Improvements

Add memory persistence

Add multi-agent coordination

Add vector database retrieval

Add authentication

Deploy on AWS

Add streaming responses

Summary (Short Version)

Built a stateful Agentic AI system using LangGraph integrating Groq LLM and Tavily Web Search API. Implemented multi-step AI workflows including tool-based chatbot and automated AI news summarization pipeline using conditional graph routing and Streamlit UI.

👩‍💻 Author
Anjali Awasthi
AI Engineer | LangGraph | Agentic AI | RAG | LLM Workflows | Databricks | AWS 
