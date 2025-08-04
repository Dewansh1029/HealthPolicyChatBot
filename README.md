# 💾 Govt Health Policy Q\&A Bot (Based on National Health Policy 2017)

## 🌟 Project Description

This project is an interactive chatbot that answers questions related to Indian Government Health Policies, especially the **National Health Policy 2017**. It uses **Retrieval-Augmented Generation (RAG)** to combine document retrieval and local Large Language Models (LLMs) for accurate, context-aware question answering.

The user can ask any natural-language question such as:

* "What are the goals of National Health Policy 2017?"
* "What is Ayushman Bharat?"
* "What are the maternal health schemes in India?"

Answers are generated based on a given policy PDF file and shown along with source text chunks.

---

## 🔧 Features

* ✍️ Ask policy-related questions in natural language
* 🧵 Based on real content from health policy PDFs
* ⚡ Uses **FAISS vector store** for fast document search
* 🧠 Runs on **HuggingFace Transformers (Flan-T5)** locally
* 🌐 Frontend built using **Streamlit**
* ✉️ Source-aware answers (displays reference document chunks)

---

## 🔹 Stack / Libraries Used

| Tool                      | Purpose                                         |
| ------------------------- | ----------------------------------------------- |
| Python                    | Programming language                            |
| Streamlit                 | Web frontend for chatbot UI                     |
| LangChain                 | Document loading, chunking, and retrieval logic |
| PyMuPDF                   | Read content from PDF files                     |
| FAISS                     | Vector similarity search engine                 |
| Hugging Face Transformers | Local LLM (Flan-T5)                             |
| sentence-transformers     | Generate dense vector embeddings                |
| torch                     | Backend for transformer model                   |

---

## 📂 File Structure

```
GenPro/
├── app.py                # Main Streamlit app
├── loader.py             # PDF loading and chunking
├── vector_store.py       # Vector creation and retrieval
├── rag_chain.py          # RAG chain using Flan-T5
├── requirements.txt     # All dependencies
├── sample_policy.pdf    # Sample policy document
└── vectorstore/         # FAISS index (auto-created)
```

---

## 🚀 Setup Instructions

### 1. Clone Repository & Navigate

```bash
git clone <your-repo-url>
cd GenPro
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧐 Sample Questions to Ask

* "What are the objectives of NHP 2017?"
* "List maternal health programmes"
* "What is the focus of Ayushman Bharat?"
* "Which policies target child health?"

---

## 🌐 Source Documents

You can replace `sample_policy.pdf` with any government health policy document of your choice (e.g., Ayushman Bharat guidelines, Mission Indradhanush reports, Jan Aushadhi policy).

Make sure the filename matches the one used in `app.py` or modify it accordingly.

---

## 📄 Requirements.txt (sample)

```
streamlit
langchain>=0.2.0
langchain-community
sentence-transformers
transformers
torch
PyMuPDF
faiss-cpu
```

---

## 💡 Future Improvements

* Add multi-PDF support
* Integrate voice input (via `speechrecognition`)
* Enable user-uploaded documents
* Summarize document content
* Add context-aware follow-up questions

---

## 🎉 Credits

Developed using open-source tools and models from:

* Hugging Face
* LangChain
* PyMuPDF
* Facebook AI Research (FAISS)
* Streamlit

---

Let me know if you want to auto-generate a `README.md` for GitHub or deploy this on Streamlit Cloud!
