# 🚀 DevLens — Ask Any Website Anything

**DevLens** is a powerful QA assistant that lets you ask **natural language questions** about any website. Using LangChain's WebLoader and Google’s Gemma-2B model, it scrapes, embeds, and retrieves website content to give you precise, LLM-powered answers.

> 💡 "Paste a link. Ask a question. Get smart answers."

---

## 🔧 Tech Stack

| Technology     | Description                           | Icon |
| -------------- | ------------------------------------- | ---- |
| 🦤 LangChain   | Framework for LLM-based RAG pipelines | 🧠   |
| 🧬 FAISS       | Vector store for document retrieval   | 📚   |
| 🤗 HuggingFace | Model & embedding hosting             | 🤖   |
| 🌐 WebLoader   | Scrapes & loads content from websites | 🌎   |
| 🐍 Python      | Main programming language             | 🔧   |

---

## 📚 How It Works

1. **Load URL**: Scrape web content using LangChain WebLoader
2. **Split & Embed**: Break text into chunks and embed via MiniLM
3. **Store in FAISS**: Vector DB stores the embedded chunks
4. **Ask a Question**: Retrieve relevant content
5. **Answer**: Use Gemma-2B to generate the final response

You just have to find the content classes of a website — like `post-title`, `post-header`, `post-content`, etc.

> 🛠️ We've also included a helper script to **list all HTML classes** on a website automatically. Attach and run that file to assist your scraping process.

---

## 🚀 Get Started

### 1. Clone the Project

```bash
git clone https://github.com/itzsudipta/GitRAG.git
cd GitRAG
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Script

```bash
python devlens.py
```

### 4. Ask Questions

```bash
Enter a URL: https://someblog.com/article
Ask: What is the main topic of this article?
```

---

## 📂 Files

```bash
GitRAG/
├── devlens.py         # ✨ One main file with all logic
├── list_classes.py    # 🏷️ Helper script to list HTML classes
├── requirements.txt   # Required Python packages
└── README.md          # You are here
```

---

## 💡 Example Queries

* "What is this website about?"
* "List all frameworks mentioned."
* "Summarize the key points."

---

## 🚧 Improvements Coming Soon

* A REST API for programmatic access
* A modern frontend for a more user-friendly experience

---

## 📡 Links

* [🤖 GitHub Repo](https://github.com/itzsudipta/GitRAG)
* [LangChain Docs](https://docs.langchain.com)
* [Gemma Model](https://ai.google.dev/gemma)

---

## 🚀 Credits

Built with ❤️ by [@itzsudipta](https://github.com/itzsudipta) using LangChain, HuggingFace, FAISS, and Python.

MIT License

Sudipta Sarkar
