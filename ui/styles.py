import streamlit as st


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --pm-bg: #050816;
            --pm-panel: rgba(14, 21, 46, 0.68);
            --pm-border: rgba(130, 160, 255, 0.16);
            --pm-text: #f5f7ff;
            --pm-muted: #8f9bb8;
            --pm-blue: #27c7ff;
            --pm-purple: #8d5cff;
        }

        .stApp {
            background:
                radial-gradient(circle at 15% 10%, rgba(42, 110, 255, 0.16), transparent 30%),
                radial-gradient(circle at 85% 25%, rgba(145, 67, 255, 0.13), transparent 28%),
                linear-gradient(135deg, #030511 0%, #070b1d 52%, #040612 100%);
            color: var(--pm-text);
            font-family: 'Inter', sans-serif;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }

        [data-testid="stSidebar"] {
            background: rgba(3, 6, 18, 0.92);
            border-right: 1px solid rgba(100, 140, 255, 0.12);
        }

        [data-testid="stFileUploaderDropzone"] {
            background: rgba(11, 18, 42, 0.66);
            border: 1px dashed rgba(64, 202, 255, 0.40);
            border-radius: 24px;
            min-height: 185px;
            transition: 0.25s ease;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.05),
                0 15px 50px rgba(0,0,0,0.25);
        }

        [data-testid="stFileUploaderDropzone"]:hover {
            border-color: rgba(141, 92, 255, 0.75);
            transform: translateY(-2px);
            box-shadow:
                0 20px 60px rgba(25, 120, 255, 0.12),
                inset 0 1px 0 rgba(255,255,255,0.06);
        }

        [data-testid="stFileUploaderDropzone"] button {
            border-radius: 12px;
        }

        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 32px;
            padding: 18px 0 34px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .brand img {
            width: 92px;
            height: 92px;
            object-fit: contain;
            filter: drop-shadow(0 10px 30px rgba(40, 170, 255, 0.22));
        }

        .eyebrow {
            color: #6bdcff;
            letter-spacing: 0.18em;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .hero h1 {
            margin: 0;
            font-size: clamp(2.3rem, 5vw, 4.5rem);
            line-height: 0.95;
            letter-spacing: -0.055em;
            font-weight: 800;
            background: linear-gradient(100deg, #ffffff 15%, #73dcff 52%, #9a73ff 90%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            color: var(--pm-muted);
            font-size: 1rem;
            margin-top: 14px;
            max-width: 680px;
        }

        .online {
            padding: 10px 15px;
            border: 1px solid rgba(66, 225, 173, 0.20);
            border-radius: 999px;
            background: rgba(23, 106, 83, 0.10);
            color: #6ff2c4;
            white-space: nowrap;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.08em;
        }

        .section-label {
            color: #7382a4;
            font-size: 0.70rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            margin: 12px 0 10px;
        }

        .glass-card {
            background: linear-gradient(
                145deg,
                rgba(19, 30, 63, 0.78),
                rgba(8, 13, 31, 0.64)
            );
            border: 1px solid var(--pm-border);
            border-radius: 24px;
            padding: 22px;
            box-shadow:
                0 20px 70px rgba(0,0,0,0.26),
                inset 0 1px 0 rgba(255,255,255,0.045);
            backdrop-filter: blur(18px);
        }

        .status-title {
            color: #9aa8c8;
            font-size: 0.68rem;
            letter-spacing: 0.16em;
            font-weight: 800;
        }

        .status-doc {
            color: white;
            font-weight: 700;
            font-size: 1.02rem;
            margin: 9px 0 18px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 9px;
        }

        .metric {
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.055);
            border-radius: 16px;
            padding: 13px 10px;
        }

        .metric .value {
            color: white;
            font-size: 1.1rem;
            font-weight: 800;
        }

        .metric .label {
            color: #7f8ba8;
            font-size: 0.62rem;
            margin-top: 4px;
        }

        .ready {
            margin-top: 16px;
            color: #72f3c5;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.1em;
        }

        .empty-chat {
            position: relative;
            min-height: 390px;
            padding: 46px 24px 28px;
            text-align: center;
            overflow: hidden;
            border: 1px solid rgba(100, 140, 255, 0.14);
            border-radius: 28px;
            background:
                radial-gradient(circle at 50% 25%, rgba(49, 166, 255, 0.11), transparent 27%),
                rgba(8, 13, 30, 0.52);
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.035),
                0 25px 90px rgba(0,0,0,0.20);
        }

        .empty-chat h2 {
            margin: 12px 0 5px;
            font-size: 1.65rem;
        }

        .empty-chat p {
            color: var(--pm-muted);
            margin: 0 auto 24px;
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 9px;
        }

        .suggestions span {
            border: 1px solid rgba(105, 151, 255, 0.14);
            background: rgba(255,255,255,0.025);
            color: #a7b3ce;
            border-radius: 999px;
            padding: 9px 13px;
            font-size: 0.72rem;
        }

        .orb {
            width: 110px;
            height: 110px;
            margin: 0 auto;
            position: relative;
            display: grid;
            place-items: center;
        }

        .orb-core {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: radial-gradient(circle at 35% 30%, #b8f5ff, #29c8ff 34%, #6c51ff 72%, #17153c 100%);
            box-shadow:
                0 0 22px rgba(39,199,255,0.75),
                0 0 70px rgba(118,83,255,0.36);
            animation: breathe 3.2s ease-in-out infinite;
        }

        .orb-ring {
            position: absolute;
            inset: 5px;
            border-radius: 50%;
            border: 1px solid rgba(55, 210, 255, 0.25);
            transform: rotateX(67deg);
        }

        .ring-2 {
            inset: 17px -7px;
            transform: rotateY(67deg) rotateX(12deg);
            border-color: rgba(151, 101, 255, 0.25);
        }

        .ring-3 {
            inset: -5px 15px;
            transform: rotateY(72deg) rotateX(67deg);
            border-color: rgba(83, 180, 255, 0.20);
        }

        @keyframes breathe {
            0%, 100% { transform: scale(0.94); opacity: 0.86; }
            50% { transform: scale(1.07); opacity: 1; }
        }

        .message {
            padding: 16px 18px;
            border-radius: 20px;
            margin: 10px 0;
            max-width: 88%;
            border: 1px solid rgba(120, 150, 255, 0.10);
        }

        .message-user {
            margin-left: auto;
            background: linear-gradient(135deg, rgba(39, 121, 255, 0.24), rgba(105, 64, 255, 0.20));
        }

        .message-assistant {
            margin-right: auto;
            background: rgba(14, 21, 44, 0.78);
        }

        .message-role {
            color: #7382a4;
            font-size: 0.64rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .source-box {
            margin-top: 14px;
            padding: 12px 14px;
            border-radius: 15px;
            background: rgba(0,0,0,0.18);
            border: 1px solid rgba(104, 148, 255, 0.10);
        }

        .source-title {
            color: #7bdfff;
            font-size: 0.67rem;
            font-weight: 800;
            letter-spacing: 0.10em;
            text-transform: uppercase;
        }

        .source-meta {
            color: #8f9bb8;
            font-size: 0.72rem;
            margin-top: 4px;
        }

        .source-text {
            color: #aeb8cf;
            font-size: 0.74rem;
            line-height: 1.5;
            margin-top: 8px;
        }

        .side-brand {
            text-align: center;
            padding: 8px 0 22px;
        }

        .side-brand img {
            width: 120px;
            height: 120px;
            object-fit: contain;
        }

        .side-brand-title {
            font-weight: 800;
            font-size: 1.1rem;
            letter-spacing: -0.02em;
        }

        .side-brand-sub {
            color: #727f9e;
            font-size: 0.68rem;
            margin-top: 4px;
        }

        @media (max-width: 900px) {
            .hero {
                align-items: flex-start;
            }
            .online {
                display: none;
            }
            .metrics {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
