import streamlit as st
import json
import pyperclip
from pathlib import Path
from src.call_llm import call_llm
from src.utils import convert_doc_to_json
from src.default_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT_SUGGESTION,
    USER_PROMPT_BETTER_TEXT,
)
from src.secrets import LLM_MODEL

st.title("RedNote Doc Review", anchor="center")
st.write("Upload RedNote documents for automatic review")
st.write(f"Backbone LLM: `{LLM_MODEL}`")

# API key input
api_key = st.text_input("Enter your OpenRouter API key:", type="password")

# File upload
example_files = list(Path("doc_to_review").glob("*.docx"))
uploaded_files = st.file_uploader(
    "Choose RedNote doc files, try to play around with some `docx` files : )",
    type=["docx"],
    accept_multiple_files=True,
)

if uploaded_files:
    # Convert doc to JSON
    json_contents = []
    for file in uploaded_files:
        json_content = convert_doc_to_json(file)
        json_contents.append(json_content)
    st.success(f"{len(json_contents)} documents successfully converted to JSON")

    # Prompt input
    system_prompt = st.text_area(
        "Enter your system prompt:", value=SYSTEM_PROMPT, height=100
    )

    user_prompt_suggestion = st.text_area(
        "Customize your user prompt for suggestion:",
        value=USER_PROMPT_SUGGESTION,
        height=150,
    )

    user_prompt_better_text = st.text_area(
        "Customize your user prompt for better text:",
        value=USER_PROMPT_BETTER_TEXT,
        height=150,
    )

    review_button = st.button("Review Document", use_container_width=True)
    if review_button:
        # Process each document
        progress_bar = st.progress(0)
        for i, json_content in enumerate(json_contents):
            progress_bar.progress((i + 1) / len(json_contents))
            content = json.loads(json_content)["content"]
            full_text = "\n".join(content)

            st.write(f"\n### Document {i+1}")

            # Get suggestions
            with st.spinner("Getting suggestions... This may take a few moments."):
                suggestion_response = call_llm(
                    system_prompt, user_prompt_suggestion, full_text, api_key=api_key
                )

            # Get better text
            with st.spinner("Getting improved text... This may take a few moments."):
                better_text_response = call_llm(
                    system_prompt, user_prompt_better_text, full_text, api_key=api_key
                )

            # Display suggestion with copy button
            st.subheader("Suggestion")
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.write(suggestion_response)
            with col2:
                if st.button("📋", key=f"suggestion_{i}"):
                    pyperclip.copy(suggestion_response)
                    st.toast("Suggestion copied to clipboard!")

            # Display better text with copy button
            st.subheader("Better Text")
            col3, col4 = st.columns([0.9, 0.1])
            with col3:
                st.write(better_text_response)
            with col4:
                if st.button("📋", key=f"better_text_{i}"):
                    pyperclip.copy(better_text_response)
                    st.toast("Better text copied to clipboard!")
