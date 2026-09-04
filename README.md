# 🤖 AI Tutor

An AI-powered tutor application built using **Python, Streamlit, LangChain, and Google Gemini**.

## 📌 Features

* 🤖 AI-powered explanations
* 📚 Explains topics for beginners
* 🧠 Uses Google Gemini
* 🔗 Built with LangChain
* 🎨 Simple and clean Streamlit UI
* ⚡ Real-time AI responses

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Google Gemini
* LangChain Google GenAI

## 📂 Project Structure

```text
AI-Tutor/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go inside the project folder:

```bash
cd AI-Tutor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

This project requires a Google Gemini API key.

Set the following environment variable:

```text
GEMINI_API_KEY
```

Do not add your actual API key to the source code or GitHub repository.

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

1. User enters a topic.
2. Streamlit receives the topic.
3. LangChain creates the prompt.
4. Google Gemini generates the explanation.
5. The result is displayed in the Streamlit interface.

## 👨‍💻 Author

Neel Shah
