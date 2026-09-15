from pathlib import Path
import base64

import streamlit as st


LOGO_PATH = Path(__file__).resolve().parent.parent / "assets" / "logo.png"


def logo_data_uri() -> str:
    data = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{data}"


def render_header():
    logo = logo_data_uri()
    st.markdown(
        f"""
        <div class="hero">
            <div class="brand">
                <img src="{logo}" alt="PolicyMind logo">
                <div>
                    <div class="eyebrow">AI-powered HR knowledge</div>
                    <h1>PolicyMind</h1>
                    <p>
                        Your intelligent HR Policy Assistant — search, understand,
                        and retrieve answers directly from your organization's policy.
                    </p>
                </div>
            </div>
            <div class="online">● SYSTEM ONLINE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_knowledge_card(document_name=None, stats=None):
    if not stats:
        st.markdown(
            """
            <div class="glass-card">
                <div class="status-title">KNOWLEDGE BASE</div>
                <div class="status-doc">No policy loaded</div>
                <div class="metrics">
                    <div class="metric"><div class="value">—</div><div class="label">PAGES</div></div>
                    <div class="metric"><div class="value">—</div><div class="label">CHUNKS</div></div>
                    <div class="metric"><div class="value">—</div><div class="label">VECTOR DIM</div></div>
                </div>
                <div class="ready">○ WAITING FOR DOCUMENT</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(
        f"""
        <div class="glass-card">
            <div class="status-title">KNOWLEDGE BASE</div>
            <div class="status-doc">📄 {document_name}</div>
            <div class="metrics">
                <div class="metric"><div class="value">{stats['pages']}</div><div class="label">PAGES</div></div>
                <div class="metric"><div class="value">{stats['chunks']}</div><div class="label">CHUNKS</div></div>
                <div class="metric"><div class="value">{stats['embedding_dimension']}</div><div class="label">VECTOR DIM</div></div>
            </div>
            <div class="ready">● FAISS KNOWLEDGE INDEX READY</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chat_message(role, content, sources):
    css_role = "message-user" if role == "user" else "message-assistant"
    label = "YOU" if role == "user" else "POLICYMIND"

    st.markdown(
        f"""
        <div class="message {css_role}">
            <div class="message-role">{label}</div>
            <div>{content}</div>
        """,
        unsafe_allow_html=True,
    )

    if sources:
        for source in sources[:3]:
            excerpt = source["text"].replace("<", "&lt;").replace(">", "&gt;")
            if len(excerpt) > 260:
                excerpt = excerpt[:260] + "..."

            st.markdown(
                f"""
                <div class="source-box">
                    <div class="source-title">◈ Source</div>
                    <div class="source-meta">
                        HR Policy • Page {source['page']} • Similarity {source['score']}
                    </div>
                    <div class="source-text">{excerpt}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


def render_sidebar(document_name=None, stats=None, on_clear=None):
    with st.sidebar:
        logo = logo_data_uri()

        st.markdown(
            f"""
            <div class="side-brand">
                <img src="{logo}" alt="PolicyMind">
                <div class="side-brand-title">PolicyMind</div>
                <div class="side-brand-sub">HR POLICY INTELLIGENCE</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Control Center")

        if stats:
            st.success("Knowledge base ready")
            st.write(f"**Document:** {document_name}")
            st.write(f"**Pages:** {stats['pages']}")
            st.write(f"**Chunks:** {stats['chunks']}")
            st.write(f"**Embeddings:** {stats['embedding_dimension']}D")
        else:
            st.info("Upload an HR policy PDF to begin.")

        if st.button("Clear document", use_container_width=True):
            if on_clear:
                on_clear()
            st.session_state.document_name = None
            st.session_state.document_stats = None
            st.session_state.messages = []
            st.rerun()

        st.markdown("---")
        st.caption(
            "Built with Streamlit • PyMuPDF • Sentence Transformers • FAISS • Groq"
        )
