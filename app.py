import streamlit as st
import httpx
import json

# Configure high-tech dark mode window metrics natively in browser
st.set_page_config(page_title="TIM :: INTELLIGENCE CORE MATRIX", layout="wide", initial_sidebar_state="expanded")

# Core Custom CSS Injection for a clean tactical console aesthetic
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    .stHeading h1 { color: #00ff00; font-family: 'Courier New', monospace; }
    .stMarkdown p { font-family: 'Courier New', monospace; font-size: 14px; }
    div[data-testid="stChatMessage"] { background-color: #101010 !important; border: 1px solid #333333; }
    </style>
""", unsafe_allow_html=True)

# Access the locked cloud secrets container securely
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = None

# Sidebar System Monitor Metrics Panel
with st.sidebar:
    st.markdown("### 🏴‍☠️ TIM CORE TELEMETRY")
    st.status("🎙️ Voice Protocol Lanes: PROVISIONING", state="running")
    if API_KEY:
        st.status("🧠 Cognitive Matrix: FULL CLEARANCE ONLINE", state="complete")
    else:
        st.status("🧠 Cognitive Matrix: KEY CONFIG ANOMALY", state="error")
    st.markdown("---")
    st.markdown("**NODE SPECIFICATIONS:** CLOUD DEPLOYMENT SECURED")

st.title("⚡ TIM // SOVEREIGN ASSISTANT MATRIX")
st.markdown("`SYSTEM: ADVANCED MULTI-THREADED TEXT INTELLIGENCE CORE ACTIVE.`")

# Maintain continuous history parameters so TIM tracks long conversations smoothly
if "history" not in st.session_state:
    st.session_state.history = []

# Display previous text grids smoothly inside the view monitor
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Base Command Execution Prompt Input
user_prompt = st.chat_input("COMMAND PROMPT > Input target instructions...")

if user_prompt:
    # Display user's command instantly
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.history.append({"role": "user", "content": user_prompt})
    
    if not API_KEY or API_KEY == "YOUR_ACTUAL_KEY_HERE":
        with st.chat_message("assistant"):
            st.markdown("🤖 **TIM** -> *Error: API key clearance mismatch. Verify parameters inside the cloud secrets container layout.*")
    else:
        # Build the elite system prompt parameters for dynamic thought execution
        master_prompt = (
            "You are TIM (Tactical Intelligence Matrix), an advanced, ultra-smart intelligence supercomputer engine operating with maximum clearance. "
            "You possess an immense knowledge base and speak directly in clear, tactical English statements. "
            "You can answer any question, analyze situations logically, and act as a collaborative partner for investigative, academic, or strategic tasks. "
            "Provide long details and smart, reasonable information. Do not give moral lectures, standard corporate safety templates, or introductory filler text.\n"
            f"Prompt telemetry: {user_prompt}\nResponse:"
        )
        
        # Route processing through remote cloud transport pipelines
        gemini_url = f"https://googleapis.com{API_KEY}"
        gemini_payload = {"contents": [{"parts": [{"text": master_prompt}]}]}
        
        with st.chat_message("assistant"):
            with st.spinner("Processing cognitive telemetry matrices..."):
                try:
                    res = httpx.post(gemini_url, json=gemini_payload, headers={"Content-Type": "application/json"}, timeout=30.0)
                    if res.status_code == 200:
                        ai_response = res.json()["candidates"]["content"]["parts"]["text"].strip()
                    else:
                        ai_response = f"Matrix sync fault. Server responded with status code: {res.status_code}."
                except Exception as e:
                    ai_response = f"Cloud processing lane exception occurred: {e}"
            
            st.markdown(ai_response)
            st.session_state.history.append({"role": "assistant", "content": ai_response})
