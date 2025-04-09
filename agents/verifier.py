def verify_summary(summary, llm):
    prompt = f"Verify the factual accuracy and completeness of this summary:\n{summary}\n\nHighlight any issues."
    return llm(prompt)