# 🤖 LangChain Q&A Chatbot

A lightweight, interactive Q&A chatbot built with **LangChain**, **Groq (LLaMA 3.1)**, and **Streamlit** — deployed live on Hugging Face Spaces.

[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/SomeshSalunkhe/Langchain_chatbot)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-orange)](https://groq.com/)

---

## 🌐 Live Demo

Try the deployed app directly on Hugging Face Spaces:  
👉 **[https://huggingface.co/spaces/SomeshSalunkhe/Langchain_chatbot](https://huggingface.co/spaces/SomeshSalunkhe/Langchain_chatbot)**

---

## 📌 Overview

This project demonstrates how to build a conversational Q&A chatbot using the LangChain framework integrated with Groq's ultra-fast inference API. The chatbot uses the **LLaMA 3.1 8B Instant** model to answer user questions in real time through a clean Streamlit web interface.

The repository also includes a `basics/` notebook that walks through foundational LangChain concepts, making it useful both as a deployable application and a learning resource.

---

## ✨ Features

- 🔗 **LangChain-powered** — modular LLM integration using `langchain-groq`
- ⚡ **Groq inference** — blazing-fast responses via the LLaMA 3.1 8B Instant model
- 🖥️ **Streamlit UI** — simple, interactive web interface for question answering
- 🔐 **Secure API key handling** — environment variable management via `python-dotenv`
- 📓 **LangChain basics notebook** — introductory Jupyter notebook for learning LangChain fundamentals
- ☁️ **Deployed on Hugging Face Spaces** — publicly accessible without any local setup

---

## 🗂️ Project Structure

```
Langchain_Chatbot/
│
├── Chat_Bot/
│   └── app.py               # Main Streamlit chatbot application
│
├── basics/
│   └── langchain.ipynb      # Jupyter notebook covering LangChain basics
│
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Component       | Technology                        |
|----------------|-----------------------------------|
| LLM Framework  | LangChain (`langchain`, `langchain-community`) |
| LLM Model      | LLaMA 3.1 8B Instant (via Groq)  |
| Inference API  | [Groq API](https://groq.com/)    |
| Frontend UI    | Streamlit                         |
| Deployment     | Hugging Face Spaces               |
| Env Management | python-dotenv                     |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Somesh-Salunkhe/Langchain_Chatbot.git
cd Langchain_Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
API=your_groq_api_key_here
```

> 🔑 Get your free Groq API key at [https://console.groq.com](https://console.groq.com)

### 5. Run the App

```bash
cd Chat_Bot
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🧠 How It Works

1. The user enters a question in the Streamlit text input field.
2. The query is passed to `get_model_response()`, which initializes a `ChatGroq` LLM instance using the LLaMA 3.1 8B Instant model.
3. LangChain's `.invoke()` method sends the query to the Groq API and retrieves the response.
4. The answer is displayed on the Streamlit UI upon clicking **Submit**.

```
User Input → LangChain ChatGroq → Groq API (LLaMA 3.1 8B) → Response → Streamlit UI
```

**Model Configuration:**
- **Model:** `llama-3.1-8b-instant`
- **Temperature:** `0.5` (balanced creativity and accuracy)
- **Max Tokens:** `1024`

---

## 📓 LangChain Basics Notebook

The `basics/langchain.ipynb` notebook covers foundational LangChain concepts including:

- Setting up LangChain with different LLM providers
- Working with prompt templates
- Building simple chains
- Understanding LangChain's invocation and response patterns

This notebook is a great starting point for anyone new to LangChain.

---

## 📦 Dependencies

```txt
langchain
langchain-groq
python-dotenv
langchain-community
streamlit
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## ☁️ Deployment on Hugging Face Spaces

This app is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/SomeshSalunkhe/Langchain_chatbot) using Streamlit as the SDK.

To deploy your own version:

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces) with **Streamlit** as the SDK.
2. Push your repository code to the Space.
3. Add your `API` (Groq API key) as a **Secret** in the Space settings under *Settings → Repository secrets*.
4. The app will build and deploy automatically.

---

## 🔐 Environment Variables

| Variable | Description                  |
|----------|------------------------------|
| `API`    | Your Groq API key            |

> ⚠️ Never commit your `.env` file or API keys to version control. The `.gitignore` is already configured to exclude `.env`.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👤 Author

**Somesh Salunkhe**  
🔗 [GitHub](https://github.com/Somesh-Salunkhe) | 🤗 [Hugging Face](https://huggingface.co/SomeshSalunkhe)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
