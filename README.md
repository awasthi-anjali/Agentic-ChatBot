### ![Watch Demo]
https://github.com/user-attachments/assets/5f9ece7c-3975-4f52-9bc3-d6c2db2f38aa


#  LangGraph Agentic AI Application

> **Stateful Agentic AI System using LangGraph, Groq LLM, and Tavily Search**


##  Overview

This project is a **production-style Agentic AI system** that orchestrates **stateful workflows** using LangGraph.

It integrates:

* 🤖 **Groq LLM (LLaMA models)**
* 🌐 **Tavily Web Search API**
* 🎨 **Streamlit UI**

Supports:

* 🗣️ Chatbot
* 🌍 Tool-augmented chatbot
* 📰 AI News automation pipeline

---

##  Tech Stack

* **LangGraph** – Workflow orchestration
* **Groq LLM** – Fast inference (LLaMA models)
* **Tavily API** – Real-time web search
* **Streamlit** – UI layer
* **Python** – Core backend

---

# 🏗️ Architecture Diagram

```mermaid
flowchart TD
    A[User Input via Streamlit UI] --> B[Main Controller]
    B --> C[Load LLM<br/>Groq]
    B --> D[Select Use Case]

    D --> E1[Basic Chatbot]
    D --> E2[Chatbot with Tool]
    D --> E3[AI News Pipeline]

    E1 --> F1[LLM Response]

    E2 --> F2{Tool Required?}
    F2 -- Yes --> G[Tavily Search Tool]
    G --> H[LLM Final Response]
    F2 -- No --> H

    E3 --> I[Fetch News]
    I --> J[Summarize via LLM]
    J --> K[Save Markdown]

    F1 --> Z[Display Output]
    H --> Z
    K --> Z
```

---

# ⚙️ High-Level Workflow

```mermaid
flowchart LR
    A[Start] --> B[Load UI]
    B --> C[User Input]
    C --> D[Select Use Case]
    D --> E[Load LLM]
    E --> F[Build Graph]
    F --> G[Execute Graph]
    G --> H[Display Output]
```

---

# 📂 Project Structure

```bash
app.py
src/
├── LanggraphAgenticAI/
│   ├── main.py
│   ├── Graph/
│   │   └── graph_builder.py
│   ├── Nodes/
│   │   ├── basic_chatbot_node.py
│   │   ├── chatbot_with_tool_node.py
│   │   └── ai_news_node.py
│   ├── Tools/
│   │   └── search_tool.py
│   ├── state/
│   │   └── state.py
│   ├── LLMS/
│   │   └── groqllm.py
│   └── UI/
│       ├── uiconfigfile.ini
│       ├── uiconfigfile.py
│       └── StreamlitUI/
│           ├── loadui.py
│           └── display_result.py
```

---

#  Core Concepts

##  Stateful AI System

```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

* Maintains conversation context
* Enables multi-step reasoning

---

# 🤖 Use Case 1: Basic Chatbot

```mermaid
flowchart TD
    A[Start] --> B[Chatbot Node]
    B --> C[End]
```

* Direct LLM interaction
* Simple conversational flow

---

# 🌍 Use Case 2: Chatbot with Web Search

```mermaid
flowchart TD
    A[Start] --> B[Chatbot]
    B --> C{Tool Needed?}
    C -- Yes --> D[Tavily Search]
    D --> E[Chatbot]
    C -- No --> E
    E --> F[End]
```

### ⚙️ How it works:

* LLM decides tool usage
* Executes web search
* Returns enriched response

 Uses: `tools_condition`
Enables **true agentic behavior**

---

# 📰 Use Case 3: AI News Pipeline

```mermaid
flowchart TD
    A[Start] --> B[Fetch News]
    B --> C[Summarize via LLM]
    C --> D[Save Markdown]
    D --> E[End]
```

###  Pipeline Steps

1. Fetch latest AI news (Tavily API)
2. Summarize using LLM
3. Save as markdown file

📁 Output:

```
./AINews/daily_summary.md
```

---

#  System Layers

## 1️⃣ Entry Point (`app.py`)

* Launches Streamlit app

## 2️⃣ Controller (`main.py`)

* Handles:

  * UI loading
  * Input processing
  * Graph execution

## 3️⃣ UI Layer

* Dynamic config via `.ini`
* Stores user inputs
* Clean modular design

## 4️⃣ LLM Layer

```python
ChatGroq(api_key, model)
```

* Dynamic model selection
* Fast inference

## 5️⃣ LangGraph Layer

* Stateful execution
* Conditional routing
* Multi-step workflows

---

#  Why This Project Stands Out

✔️ Graph-based AI architecture
✔️ Real-world agent workflows
✔️ Tool-integrated LLM system
✔️ Modular & scalable design
✔️ Production-style pipeline

>  This is NOT just a chatbot — it's a **full Agentic AI System**

---

#  Installation

## 1️⃣ Clone

```bash
git clone https://github.com/awasthi-anjali/Agentic-ChatBot.git
cd langgraph-agentic-ai
```

## 2️⃣ Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Set API Keys

* `GROQ_API_KEY`
* `TAVILY_API_KEY`

Enter via UI

---

## ▶️ Run App

```bash
streamlit run app.py
```

---

#  Use Cases

| Feature        | Description             |
| -------------- | ----------------------- |
| 🗣️ Chatbot    | Basic LLM interaction   |
| 🌍 Web Chatbot | LLM + Search tool       |
| 📰 AI News     | Automated news pipeline |

---

#  Future Improvements

* Memory persistence
* Multi-agent collaboration
* Vector database (RAG)
* Authentication system
* AWS deployment
* Streaming responses

---

# Summary

> Built a **stateful Agentic AI system using LangGraph**, integrating Groq LLM and Tavily Web Search API. Designed multi-step AI workflows with conditional routing, tool-based reasoning, and a Streamlit UI for real-time interaction.

---

<img width="1899" height="884" alt="Basic-Chatbot" src="https://github.com/user-attachments/assets/c1a1d695-cb00-43f0-986e-4893b5351148" />
<img width="1901" height="913" alt="Chatbot with web" src="https://github.com/user-attachments/assets/7ce3179a-668f-4dd7-b83f-c3649c2f59b4" />
<img width="1887" height="903" alt="AI news" src="https://github.com/user-attachments/assets/7eb75f57-4c26-453c-aadd-f9d0f6ab22ab" />



