from openai import OpenAI
from src.secrets import API_KEY, API_BASE_URL, LLM_MODEL
from src.default_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT_SUGGESTION,
    USER_PROMPT_BETTER_TEXT,
)


def call_llm(
    system_prompt,
    user_prompt,
    text,
    api_key=API_KEY,
    api_base_url=API_BASE_URL,
    llm_model=LLM_MODEL,
):
    """Call DeepSeek API to get document review"""

    client = OpenAI(
        base_url=api_base_url,
        api_key=api_key,
    )

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://rednote-doc-review.streamlit.app",
                "X-Title": "RedNote Doc Review",
            },
            model=llm_model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt.format(text),
                },
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error calling OpenRouter API: {str(e)}"
