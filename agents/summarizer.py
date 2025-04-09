def summarize_docs(docs, llm):
    content = "\n".join([doc.page_content for doc in docs])
    prompt = f"Summarize the following academic content in a clear, concise way:\n{content}"
    return llm(prompt)