import streamlit as st
from loader import load_and_split_pdf
from vector_store import create_vector_store, load_vector_store
from rag_chain import get_rag_chain
import os

st.set_page_config(page_title="Govt Policy Q&A Bot", layout="centered")
st.title("🧾 Govt Health Policy 2017 Q&A Bot")

pdf_path = "sample_policy.pdf"  # Make sure this file exists in the same directory

# Step 1: Index the PDF if not already indexed
if not os.path.exists("vectorstore"):
    st.info("⏳ Indexing document, please wait...")
    chunks = load_and_split_pdf(pdf_path)
    create_vector_store(chunks)

# Step 2: Load vector store and build RAG chain
vector_store = load_vector_store()
qa_chain = get_rag_chain(vector_store)

# Step 3: Ask user for input
query = st.text_input("🔍 Ask a question:").strip()

# Optional guidance
st.markdown("""
💡 Example questions:
- What is the objective of Ayushman Bharat?
- What are the components of National Health Mission?
- What does NHP 2017 focus on?
""")

# Step 4: Handle query
if query:
    # Filter out irrelevant or out-of-scope questions
    banned_keywords = ["who is", "your name", "where are you", "who are you", "creator", "developer"]
    if any(bad in query.lower() for bad in banned_keywords):
        st.warning("🤖 I'm trained only on health policy documents. Please ask about healthcare programs, policies, or government schemes.")
    elif len(query.split()) <= 2:
        st.warning("❗ Please ask a more specific question (more than 2 words).")
    else:
        with st.spinner("Thinking..."):
            result = qa_chain.invoke({"query": query})
            answer = result.get("result", "").strip()
            source_docs = result.get("source_documents", [])

            # Validate result quality
            if not answer or len(source_docs) == 0 or all(len(doc.page_content.strip()) < 50 for doc in source_docs):
                st.warning("⚠️ Sorry, I couldn't find a reliable answer in the document.")
            else:
                st.write("🧠 **Answer:**", answer)
                with st.expander("📄 Source(s):"):
                    for i, doc in enumerate(source_docs):
                        st.markdown(f"**Chunk {i+1}:** {doc.page_content[:300]}...")
