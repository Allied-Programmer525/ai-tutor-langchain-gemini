
import streamlit as st
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Gemini API Key
# -----------------------------

api_key = st.secrets["GEMINI_API_KEY"]

if not api_key:
    st.error("Gemini API key not found.")
    st.stop()




# -----------------------------
# UI
# -----------------------------

st.title("🤖 AI Tutor")

st.write(
    "Enter any topic and the AI will explain it "
    "in simple language."
)


# -----------------------------
# LangChain + Gemini
# -----------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.7,
    google_api_key=api_key
)


prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI tutor.

    Explain {topic} to a complete beginner.

    Use simple language and one real world example.
    """
)


chain = prompt | llm | StrOutputParser()


# -----------------------------
# User Input
# -----------------------------

topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Quantum Physics"
)


# -----------------------------
# Generate Answer
# -----------------------------

if st.button("Explain Topic"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("AI is thinking..."):

            try:

                result = chain.invoke({
                    "topic": topic
                })

                st.subheader("📚 Explanation")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")
