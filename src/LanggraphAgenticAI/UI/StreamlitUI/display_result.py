import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from textwrap import dedent
from html import escape


CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap');

/* ── Root & Global ─────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Sidebar ───────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #d6e8f5 !important;
    border-right: 1px solid #b6cfe0 !important;
}

[data-testid="stSidebar"] * {
    color: #1a3a52 !important;
}

/* Sidebar header / title */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    color: #1a3a52 !important;
    letter-spacing: -0.3px;
}

/* Sidebar selectbox / radio labels */
[data-testid="stSidebar"] label {
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.6px !important;
    text-transform: uppercase !important;
    color: #4a7a99 !important;
}

/* Sidebar radio buttons active */
[data-testid="stSidebar"] [data-testid="stRadio"] div[aria-checked="true"] {
    background: #3a7aab !important;
    color: white !important;
    border-radius: 8px;
}

/* Sidebar selectbox */
[data-testid="stSidebar"] .stSelectbox select,
[data-testid="stSidebar"] div[data-baseweb="select"] {
    background: #e8f2fa !important;
    border: 1px solid #a0c4dc !important;
    border-radius: 8px !important;
    color: #1a3a52 !important;
}

/* Sidebar divider */
[data-testid="stSidebar"] hr {
    border-color: #b6cfe0 !important;
}

/* ── Run / Submit Button (GREEN) ───────────────────────────── */
[data-testid="stSidebar"] .stButton > button,
[data-testid="stSidebar"] button[kind="primary"],
.stButton > button[kind="primary"] {
    background: #2ea84f !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.2px !important;
    padding: 10px 20px !important;
    box-shadow: 0 2px 10px rgba(46, 168, 79, 0.35) !important;
    transition: all 0.15s ease !important;
    width: 100%;
}

[data-testid="stSidebar"] .stButton > button:hover,
.stButton > button[kind="primary"]:hover {
    background: #27963f !important;
    box-shadow: 0 4px 14px rgba(46, 168, 79, 0.45) !important;
    transform: translateY(-1px) !important;
}

/* ── Main Chat Area ────────────────────────────────────────── */
.main .block-container,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"] {
    background: #2e3d4e !important;
}

.stApp {
    background: #2e3d4e !important;
}

/* ── App Header / Title ────────────────────────────────────── */
h1.app-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 22px !important;
    color: #d0e8f8 !important;
    letter-spacing: -0.4px !important;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── Chat Messages ─────────────────────────────────────────── */
[data-testid="stChatMessage"] {
    border-radius: 12px !important;
    margin-bottom: 8px !important;
}

/* Chat content color */
[data-testid="stChatMessageContent"] p,
[data-testid="stChatMessageContent"] span,
[data-testid="stChatMessageContent"] li {
    color: #c8dff0 !important;
}

/* Avatar shells */
[data-testid="stChatMessageAvatarUser"] > div,
[data-testid="stChatMessageAvatarAssistant"] > div {
    border-radius: 50% !important;
}

/* User bubble */
[data-testid="stChatMessageAvatarUser"] + div {
    background: #2ea84f !important;
    color: #ffffff !important;
    border-radius: 12px !important;
}

/* AI / assistant bubble */
[data-testid="stChatMessageAvatarAssistant"] + div {
    background: #3a4f63 !important;
    color: #c8dff0 !important;
    border: 1px solid #4a6070 !important;
    border-radius: 12px !important;
}

/* Avatar icons */
[data-testid="stChatMessageAvatarUser"] svg {
    background: #2ea84f !important;
    border-radius: 50%;
}
[data-testid="stChatMessageAvatarAssistant"] svg {
    background: #3a7aab !important;
    border-radius: 50%;
}

/* ── Tool Call Blocks ──────────────────────────────────────── */
.tool-call-block {
    background: #243344;
    border-left: 3px solid #3a7aab;
    border-radius: 8px;
    padding: 10px 14px;
    color: #7aabcc;
    font-size: 12px;
    font-family: 'DM Mono', 'Courier New', monospace;
    margin: 4px 0;
}

/* ── Spinner ───────────────────────────────────────────────── */
.stSpinner > div {
    border-color: #3a7aab transparent transparent !important;
}

/* ── Markdown in main ──────────────────────────────────────── */
.block-container p,
.block-container li,
.block-container span {
    color: #c8dff0 !important;
    font-family: 'DM Sans', sans-serif !important;
    line-height: 1.65 !important;
}

.block-container h1, .block-container h2, .block-container h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #d0e8f8 !important;
}

/* ── Input Box ─────────────────────────────────────────────── */
[data-testid="stChatInputTextArea"] {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #c7d4df !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stChatInputTextArea"] textarea,
[data-testid="stChatInputTextArea"] input {
    color: #111111 !important;
    caret-color: #111111 !important;
}

[data-testid="stChatInputTextArea"] textarea::placeholder {
    color: #5f6b75 !important;
}

[data-testid="stChatInputTextArea"]:focus {
    border-color: #3a7aab !important;
    box-shadow: 0 0 0 2px rgba(58, 122, 171, 0.25) !important;
}

/* Send button in chat input */
[data-testid="stChatInputSubmitButton"] {
    background: #2ea84f !important;
    border-radius: 8px !important;
}

/* ── Scrollbar ─────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #4e6478; border-radius: 4px; }
</style>
"""

ROBOT_SVG = """
<svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="44" height="44" rx="12" fill="#3a7aab"/>
  <rect x="11" y="16" width="22" height="16" rx="4" fill="#d6e8f5"/>
  <rect x="15" y="21" width="5" height="5" rx="1.5" fill="#3a7aab"/>
  <rect x="24" y="21" width="5" height="5" rx="1.5" fill="#3a7aab"/>
  <rect x="14" y="29" width="16" height="2" rx="1" fill="#b6cfe0"/>
  <rect x="19" y="11" width="6" height="6" rx="3" fill="#d6e8f5"/>
  <circle cx="22" cy="10" r="2.5" fill="#2ea84f"/>
  <rect x="7" y="22" width="3" height="6" rx="1.5" fill="#d6e8f5"/>
  <rect x="34" y="22" width="3" height="6" rx="1.5" fill="#d6e8f5"/>
</svg>
"""


def inject_styles():
    """Call this once at the top of your Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_app_header(usecase: str = ""):
    """Renders a branded header with robot icon."""
    safe_usecase = escape(usecase if usecase else "Select a use case")
    header_html = (
        '<div style="display:flex; align-items:center; gap:12px; padding:4px 0 16px;">'
        f"{ROBOT_SVG}"
        '<div>'
        "<div style=\"font-family:'Space Grotesk',sans-serif; font-size:20px;"
        "font-weight:700; color:#d0e8f8; letter-spacing:-0.4px;\">"
        "AI Assistant"
        "</div>"
        "<div style=\"font-size:11px; color:#5a8aaa; letter-spacing:0.6px;"
        "text-transform:uppercase; margin-top:1px;\">"
        f"{safe_usecase}"
        "</div>"
        "</div>"
        "</div>"
        '<hr style="border:none; border-top:1px solid #3e5163; margin:0 0 16px;"/>'
    )
    st.markdown(header_html, unsafe_allow_html=True)


def render_App_header(usecase: str = ""):
    """Backward-compatible alias for older function naming."""
    render_app_header(usecase)


def render_tool_message(content: str):
    """Renders a tool call block with a monospace terminal style."""
    safe_content = escape(str(content)).replace("\n", "<br>")
    st.markdown(
        dedent(
            f"""
        <div style="background:#243344; border-left:3px solid #3a7aab;
                    border-radius:8px; padding:10px 14px; margin:4px 0;">
            <div style="font-size:10px; color:#5a8aaa; font-weight:600;
                        letter-spacing:0.5px; text-transform:uppercase;
                        margin-bottom:5px;">⚙ Tool Call</div>
            <div style="color:#7aabcc; font-size:12px;
                        font-family:'Courier New',monospace; line-height:1.5;">
                {safe_content}
            </div>
        </div>
        """
        ).strip(),
        unsafe_allow_html=True,
    )


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            with st.chat_message("user", avatar="👤"):
                st.write(user_message)

            assistant_placeholder = st.empty()
            assistant_text = ""
            for event in graph.stream({"messages": ("user", user_message)}):
                for value in event.values():
                    message_obj = value.get("messages")
                    if hasattr(message_obj, "content"):
                        assistant_text = message_obj.content
                    elif isinstance(message_obj, list) and message_obj and hasattr(message_obj[-1], "content"):
                        assistant_text = message_obj[-1].content
                    if assistant_text:
                        with assistant_placeholder.container():
                            with st.chat_message("assistant", avatar="🤖"):
                                st.write(assistant_text)

        elif usecase == "Chatbot with Web":
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)

            for message in res["messages"]:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user", avatar="👤"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    render_tool_message(message.content)
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant", avatar="🤖"):
                        st.write(message.content)

        elif usecase == "AI NEWS":
            frequency = self.user_message
            with st.spinner(f"Fetching and summarising {frequency.lower()} AI news…"):
                graph.invoke({"messages": [HumanMessage(content=frequency)]})
                try:
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as f:
                        markdown_content = f.read()
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News file not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")


# ── Example app entry point ──────────────────────────────────
# In your main app.py, call inject_styles() before anything else:
#
#   import streamlit as st
#   from display_result_streamlit import inject_styles, render_app_header, DisplayResultStreamlit
#
#   st.set_page_config(page_title="NexusAI", page_icon="🤖", layout="wide")
#   inject_styles()
#
#   with st.sidebar:
#       st.markdown("### ⚙ Configuration")
#       usecase = st.radio("Use Case", ["Basic Chatbot", "Chatbot with Web", "AI NEWS"])
#       if usecase == "AI NEWS":
#           frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
#       st.button("▶ Run Pipeline")   # ← automatically green via CSS
#
#   render_app_header(usecase)
#   user_message = st.chat_input("Ask something...")
#   if user_message:
#       display = DisplayResultStreamlit(usecase, graph, user_message)
#       display.display_result_on_ui()