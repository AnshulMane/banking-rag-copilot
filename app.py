import streamlit as st

from rag import create_rag
from pii import anonymize_text
from agent import banking_ai

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ASTOR",
    page_icon="🏦",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #07142b;
    color: white;
    font-family: 'Segoe UI';
}

/* MAIN TITLE */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

.sub-title {
    color: #c8d3f5;
    font-size: 18px;
    margin-bottom: 25px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #081a38;
    border-right: 1px solid #1e335c;
}

/* METRIC CARDS */
.metric-card {
    background-color: #0d2347;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
    border: 1px solid #1f3b70;
}

.metric-title {
    color: #9fb7ff;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 28px;
    font-weight: bold;
}

/* ALERT BOX */
.alert-box {
    background-color: #13294d;
    padding: 14px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 4px solid #d4af37;
}

/* USER CHAT */
.user-message {
    background-color: #12305e;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* AI RESPONSE */
.bot-message {
    background-color: #0b1f3f;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #1e3f75;
    line-height: 1.7;
}

/* BUTTON */
.stButton button {
    background-color: #d4af37;
    color: black;
    border-radius: 10px;
    font-weight: bold;
    height: 50px;
    border: none;
}

/* INPUT BOX */
textarea {
    background-color: #10284d !important;
    color: white !important;
    border-radius: 12px !important;
}

/* REMOVE STREAMLIT HEADER */
header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD RAG SYSTEM
# ==========================================

qa = create_rag()

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🏦 RM Workspace")

    st.markdown("---")

    st.markdown("## Client Intelligence")

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">UHNW Relationships</div>
        <div class="metric-value">18</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Family Offices</div>
        <div class="metric-value">6</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Cross-Border Clients</div>
        <div class="metric-value">9</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Priority Reviews</div>
        <div class="metric-value">3</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## AI Advisory Modules")

    st.markdown("""
    - Wealth Preservation Advisory  
    - Estate & Legacy Planning  
    - International Banking Insights  
    - Premium Credit Recommendations  
    - Fraud Intelligence  
    - Portfolio Risk Analysis  
    """)

    st.markdown("---")

    st.markdown("## Priority Client Alerts")

    st.markdown("""
    <div class="alert-box">
    UHNW portfolio review pending
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-box">
    Large international transfer flagged
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-box">
    Wealth migration opportunity identified
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MAIN HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🏦 ASTOR
</div>

<div class="sub-title">
Private Banking Intelligence Workspace
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# CHAT HISTORY
# ==========================================

for chat in reversed(st.session_state.messages):

    st.markdown(f"""
    <div class="user-message">
    <b>Relationship Manager</b><br><br>
    {chat["user"]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="bot-message">
    <b>ASTOR AI</b><br><br>
    {chat["bot"]}
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# USER INPUT
# ==========================================

user_input = st.text_area(
    "Relationship Manager Request",
    height=80,
    placeholder="Recommend wealth preservation strategy for a UK client with £5 million liquidity."
)

# ==========================================
# ACTION BUTTONS
# ==========================================

col1, spacer, col2 = st.columns([1, 8, 1.4])

with col1:

    ask_button = st.button(
        "Ask ASTOR",
        use_container_width=True
    )

with col2:

    clear_button = st.button(
        "Clear Workspace",
        use_container_width=True
    )

# ==========================================
# CLEAR CHAT
# ==========================================

if clear_button:

    st.session_state.messages = []

    st.rerun()

# ==========================================
# AI RESPONSE
# ==========================================

if ask_button and user_input:

    with st.spinner("Analyzing banking intelligence..."):

        try:

            # ======================================
            # PII MASKING
            # ======================================

            safe_query = anonymize_text(user_input)

            # ======================================
            # ENTERPRISE BANKING ANALYSIS
            # ======================================

            banking_analysis = banking_ai(safe_query)

            # ======================================
            # RAG KNOWLEDGE RETRIEVAL
            # ======================================

            rag_response = qa.invoke(
                {"query": safe_query}
            )

            rag_result = rag_response["result"]

            # ======================================
            # FINAL ENTERPRISE RESPONSE
            # ======================================

            final_response = f"""
{banking_analysis}

------------------------------------------------------------

Enterprise Knowledge Response
------------------------------------------------------------

{rag_result}
"""

            # ======================================
            # STORE CHAT HISTORY
            # ======================================

            st.session_state.messages.append(
                {
                    "user": user_input,
                    "bot": final_response
                }
            )

            st.rerun()

        except Exception as e:

            st.session_state.messages.append(
                {
                    "user": user_input,
                    "bot": f"""
Enterprise AI System Error

{str(e)}

Possible Causes:
- Ollama model not running
- Phi3 model unavailable
- ChromaDB issue
- Vector database missing
- Invalid enterprise query
"""
                }
            )

            st.rerun()

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
Private Banking Intelligence Platform
""")