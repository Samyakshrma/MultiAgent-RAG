import streamlit as st
from agents import retriever, summarizer, verifier, synthesizer
from langchain_openai import OpenAI  # instead of from langchain.llms

st.title("\U0001F9E0 Multi-Agent RAG Research Assistant")

query = st.text_input("Enter your research question:")

if query:
    llm = OpenAI(temperature=0)  # Swap with a local model if needed
    docs = retriever.retrieve_docs(query)

    with st.spinner("Summarizing..."):
        summary = summarizer.summarize_docs(docs, llm)

    with st.spinner("Verifying..."):
        verification = verifier.verify_summary(summary, llm)

    with st.spinner("Synthesizing final answer..."):
        final_answer = synthesizer.synthesize_answer(summary, verification, llm)

    st.subheader("\U0001F4AC Final Answer:")
    st.write(final_answer)