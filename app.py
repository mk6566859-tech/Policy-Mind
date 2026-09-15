import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from services.rag_pipeline import RAGPipeline
from ui.components import render_sidebar, render_header, render_knowledge_card, render_chat_message
from ui.styles import inject_css

st.set_page_config(
    page_title="PolicyMind — HR Policy Assistant",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

if "rag" not in st.session_state:
    st.session_state.rag = RAGPipeline()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_name" not in st.session_state:
    st.session_state.document_name = None

if "document_stats" not in st.session_state:
    st.session_state.document_stats = None

if "processing_error" not in st.session_state:
    st.session_state.processing_error = None


def process_pdf(uploaded_file):
    st.session_state.processing_error = None
    try:
        stats = st.session_state.rag.ingest_pdf(uploaded_file)
        st.session_state.document_name = uploaded_file.name
        st.session_state.document_stats = stats
        st.session_state.messages = []
    except Exception as exc:
        st.session_state.processing_error = str(exc)


render_sidebar(
    document_name=st.session_state.document_name,
    stats=st.session_state.document_stats,
    on_clear=lambda: st.session_state.rag.clear(),
)

render_header()

# Upload zone
st.markdown('<div class="section-label">01 / KNOWLEDGE BASE</div>', unsafe_allow_html=True)
upload_col, status_col = st.columns([1.35, 1], gap="large")

with upload_col:
    uploaded_file = st.file_uploader(
        "Drop your HR policy PDF here",
        type=["pdf"],
        label_visibility="collapsed",
        help="Upload one HR policy PDF to build the searchable knowledge base.",
    )

    if uploaded_file is not None:
        current_name = st.session_state.document_name
        if current_name != uploaded_file.name:
            with st.spinner("Analyzing policy • extracting text • building embeddings..."):
                process_pdf(uploaded_file)

with status_col:
    render_knowledge_card(
        document_name=st.session_state.document_name,
        stats=st.session_state.document_stats,
    )

if st.session_state.processing_error:
    st.error(f"Could not process the PDF: {st.session_state.processing_error}")

st.markdown('<div class="section-label">02 / POLICY CONVERSATION</div>', unsafe_allow_html=True)

# Chat area
chat_shell = st.container()
with chat_shell:
    if not st.session_state.messages:
        st.markdown(
            """
            <div class="empty-chat">
                <div class="orb">
                    <div class="orb-core"></div>
                    <div class="orb-ring ring-1"></div>
                    <div class="orb-ring ring-2"></div>
                    <div class="orb-ring ring-3"></div>
                </div>
                <h2>Ask your policy.</h2>
                <p>Upload an HR policy and ask questions in plain language.</p>
                <div class="suggestions">
                    <span>What is the leave policy?</span>
                    <span>Who is eligible for benefits?</span>
                    <span>What is the work-from-home policy?</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        for message in st.session_state.messages:
            render_chat_message(message["role"], message["content"], message.get("sources", []))

question = st.chat_input(
    "Ask something about your HR policy...",
    disabled=st.session_state.document_stats is None,
)

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question, "sources": []}
    )

    with st.spinner("Searching policy knowledge..."):
        try:
            answer, sources = st.session_state.rag.ask(question)
        except Exception as exc:
            answer = f"I couldn't complete the request: {exc}"
            sources = []

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )
    st.rerun()

if st.session_state.document_stats is None:
    st.caption("Upload a PDF above to activate the assistant.")
else:
    st.caption("Answers are grounded in the uploaded document. Always verify high-stakes HR decisions with your organization’s HR team.")
