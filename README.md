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

---

# ▶️ Run the Project in Google Colab

You can run this project completely inside **Google Colab** without installing Python on your computer.

## Step 1: Open Google Colab

Open a new Google Colab notebook.

## Step 2: Install Required Packages

Run this in a Colab cell:

```python
!pip install -q -U streamlit langchain langchain-google-genai pyngrok
```

## Step 3: Add Gemini API Key

Run:

```python
import os
from getpass import getpass

os.environ["GEMINI_API_KEY"] = getpass("Enter your Gemini API key: ")
```

Enter your Gemini API key when Colab asks for it.

**Do not upload or commit your API key to GitHub.**

## Step 4: Create `app.py`

If you are creating the project directly in Colab, run:

```python
%%writefile app.py
```

Then paste the complete `app.py` code below this line.

Alternatively, you can upload the `app.py` file from your GitHub repository into Colab.

## Step 5: Check the Files

Run:

```python
!ls
```

You should see:

```text
app.py
```

## Step 6: Start Streamlit

Run:

```python
!streamlit run app.py &>/content/logs.txt &
```

## Step 7: Check Streamlit Logs

Run:

```python
!cat /content/logs.txt
```

You should see that Streamlit is running on port `8501`.

## Step 8: Set Up ngrok

Import ngrok:

```python
from pyngrok import ngrok
```

Add your ngrok authentication token:

```python
ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN")
```

Replace `YOUR_NGROK_AUTHTOKEN` with your actual ngrok authentication token.

## Step 9: Create a Public URL

Run:

```python
public_url = ngrok.connect(8501)

print(public_url)
```

You will get a URL similar to:

```text
https://xxxx-xxxx.ngrok-free.app
```

Open that URL in your browser.

Your Streamlit AI Tutor application will now be accessible through the browser.

---

# 💡 How the Colab Setup Works

```text
Google Colab
     ↓
Streamlit
     ↓
localhost:8501
     ↓
ngrok
     ↓
Public URL
     ↓
AI Tutor
```

Google Colab runs the Streamlit server, while ngrok provides a public URL that forwards requests to the Streamlit server.

---

# 💻 Run Locally

If you want to run the project on your computer:

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project Folder

```bash
cd AI-Tutor
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Set the Gemini API Key

Set the `GEMINI_API_KEY` environment variable.

## 5. Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🔑 API Key Security

Never put your actual Gemini API key directly inside:

* `app.py`
* `README.md`
* `requirements.txt`
* GitHub repository

For deployment, use Streamlit's Secrets management.

---

# ☁️ Deploy on Streamlit Community Cloud

The GitHub repository can be connected to **Streamlit Community Cloud** and deployed as a web application.

During deployment, select:

```text
Repository: Your GitHub repository
Branch: main
Main file: app.py
```

Add your Gemini API key through the **Secrets** section instead of putting it in GitHub.

Streamlit Community Cloud supports deployment directly from GitHub repositories and uses your dependency file to install required Python packages.

---

# 💡 How the Application Works

1. User enters a topic.
2. Streamlit receives the topic.
3. LangChain creates the prompt.
4. Google Gemini generates the explanation.
5. The result is displayed in the Streamlit interface.

---

# 👨‍💻 Author

**Neel Shah**
