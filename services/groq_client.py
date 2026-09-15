import os

from groq import Groq


SYSTEM_PROMPT = """
You are PolicyMind, an HR policy assistant.

Answer questions using ONLY the supplied policy context.

Rules:
1. If the answer is not present in the context, say that the uploaded policy
   does not contain enough information to answer the question.
2. Do not invent HR rules, benefits, dates, eligibility requirements, or legal advice.
3. Be concise but useful.
4. When the context contains conflicting information, explicitly mention the conflict.
5. Treat the policy as organizational information, not as a substitute for legal advice.
"""


def get_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. Add it to your .env file locally "
            "or Streamlit Secrets in deployment."
        )
    return Groq(api_key=api_key)


def generate_answer(question: str, context: str) -> str:
    client = get_client()

    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    user_prompt = f"""
POLICY CONTEXT:
{context}

QUESTION:
{question}

Write the best grounded answer based only on the policy context.
"""

    response = client.chat.completions.create(
        model=model,
        temperature=0.1,
        max_tokens=700,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content.strip()
