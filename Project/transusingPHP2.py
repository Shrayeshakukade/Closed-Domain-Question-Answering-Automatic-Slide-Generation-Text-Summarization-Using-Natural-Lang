import os
import sys
from PyPDF2 import PdfFileReader
from transformers import pipeline
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

def load_qa_model():
    model = pipeline("question-answering")
    return model    


def text_extract(file_path):
    article=""
    pdfreader = PdfFileReader(file_path)
    count = pdfreader.numPages
    for i in range(count):
        page = pdfreader.getPage(i)
        article += page.extractText()
    return article

d = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/"
file_path = os.listdir(d)[0]
print(file_path)
if os.path.exists(file_path):
    #print(file_path)
    #if file_path:
    file_path = d+file_path
    content = text_extract(file_path)
    f = open("C:/xampp/htdocs/BE_Project/BE_Project/content.txt", "w", encoding='utf-8')
    f.write(content)
    #print(content)
else:
    d4 = "C:/xampp/htdocs/BE_Project/BE_Project/content.txt"
    with open(d4) as f2:
        content2 = f2.read()
    content = content2

d2 = "C:/xampp/htdocs/BE_Project/BE_Project/QuestionFile.txt"
with open(d2) as f:
    lines = f.read()
q = lines

qa = load_qa_model()
q = lines
answers = qa(question=q, context=content)
if answers['score'] < 0.40:
    ans = "Answer not found"
else:
    ans = answers['answer']
ans = answers['answer']

if(os.path.exists("C:/xampp/htdocs/BE_Project/BE_Project/answerFile.txt")):
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/answerFile.txt', 'r+')
    outfile.truncate(0)
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/answerFile.txt','w',encoding="utf-8")
    outfile.write(ans)
else:
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/answerFile.txt','w',encoding="utf-8")
    outfile.write(ans)
outfile.close
