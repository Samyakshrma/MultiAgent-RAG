def synthesize_answer(summary, verification, llm):
    prompt = f"Using the summary and verification below, generate a well-structured final answer:\n\nSummary:\n{summary}\n\nVerification Notes:\n{verification}"
    return llm(prompt)