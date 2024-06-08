import streamlit as st
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import PyPDF2
from docx import Document

def extract_text_from_pdf(uploaded_file):
    with open(uploaded_file, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_word(uploaded_file):
    doc = Document(uploaded_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

def summarize_document(input_text, max_length=150):
    # Initialize RAG tokenizer, retriever, and sequence generator
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-base", index_name="exact")
    generator = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base")

    # Encode input text
    input_dict = tokenizer(input_text, return_tensors="pt")

    # Retrieve relevant documents
    context_input_ids = retriever(input_dict["input_ids"])

    # Generate summary
    generated = generator.generate(context_input_ids["context_input_ids"], max_length=max_length)
    summary = tokenizer.decode(generated[0], skip_special_tokens=True)

    return summary

# Streamlit UI
st.set_page_config(page_title="Document Summarization Tool")
st.title("Document Summarization Tool")

document_type = st.selectbox("Select Document Type", ["Text", "PDF", "Word"])

if document_type == "Text":
    uploaded_file = st.file_uploader("Upload Text File", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read()
        st.write("### Original Text")
        st.write(text)

        summary = summarize_document(text)
        st.write("### Summary")
        st.write(summary)

elif document_type == "PDF":
    uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.write("### Original Text")
        st.write(pdf_text)

        summary = summarize_document(pdf_text)
        st.write("### Summary")
        st.write(summary)

elif document_type == "Word":
    uploaded_file = st.file_uploader("Upload Word Document", type=["docx"])
    if uploaded_file is not None:
        word_text = extract_text_from_word(uploaded_file)
        st.write("### Original Text")
        st.write(word_text)

        summary = summarize_document(word_text)
        st.write("### Summary")
        st.write(summary)
