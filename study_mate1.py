import streamlit as st
from openai import OpenAI
import PyPDF2

client = OpenAI(api_key="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")   # Use your real API key

st.set_page_config(page_title="Study Mate", layout="centered")
st.title("📘 Study Mate: Ask Questions from Your PDF")

uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            pdf_text += content

    st.success("✅ PDF text extracted successfully!")

    question = st.text_input("❓ Ask a question based on the uploaded PDF")

    if question and st.button("🔍 Get Answer"):
        with st.spinner("Analyzing PDF and generating response..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for answering questions from PDF content."},
                    {"role": "user", "content": f"Context:\n{pdf_text}\n\nQuestion:\n{question}"}
                ]
            )
            answer = response.choices[0].message.content
            st.markdown("### 📖 Answer:")
            st.write(answer)
