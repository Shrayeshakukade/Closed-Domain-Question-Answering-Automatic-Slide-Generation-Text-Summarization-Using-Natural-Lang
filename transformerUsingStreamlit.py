import PyPDF2
#from PyPDF2.pdf import ContentStream
from PyPDF2 import PdfFileReader
import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_qa_model():
    model = pipeline("question-answering")
    return model

#counfiguration
st.set_option('deprecation.showfileUploaderEncoding', False)

#add a sidebar
st.sidebar.subheader("Uplaod file here")

#setup file upload
uploaded_file = st.sidebar.file_uploader(label = "Upload pdf file", type=['pdf'], )

article = ""

if uploaded_file is not None:
    pdfreader = PdfFileReader(uploaded_file)
    count = pdfreader.numPages
    article=""
    for i in range(count):
        page = pdfreader.getPage(i)
        article += page.extractText()

qa = load_qa_model()
st.title("Ask Questions about your Text")
sentence = article
#st.write(article)
question = st.text_input("Questions from this article?")
button = st.button("Get me Answers")
with st.spinner("Discovering Answers.."):
    if button and sentence:
        answers = qa(question=question, context=sentence)
        #st.write(answers['answer'])
        if answers['score']<0.30:
            st.write("Answer not found")
        else:
            st.write(answers)
