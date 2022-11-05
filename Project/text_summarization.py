import io
import os
import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import os
import re
from heapq import nlargest
import string
from string import punctuation

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)



    fp.close()
    device.close()
    text = retstr.getvalue()
    #sentence = text.replace('\n',' ')
    sentence = text.replace('-',' ')
    sentence = sentence.replace('',' ')
    sentence = sentence.replace(';',' ')
    sentence = sentence.replace('','●')
    retstr.close()
    return sentence
    


def preprocessing(str):
    stopwords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    #str=str.lower()
    str = re.sub(' +', ' ',str)
    doc=nlp(str)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords:
            
            if word.text.lower() not in punctuation:
                
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    
                    word_frequencies[word.text] += 1    
    delete_key=' '
    word_frequencies.pop(delete_key,None)
    all_frequencies = word_frequencies.values()
    max_value = max(all_frequencies)
    for word in word_frequencies:
        #normalization of word frequencies
        word_frequencies[word] = word_frequencies[word]/max_value

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    
    for sent in sentence_tokens:
        
        for word in sent:
            
            if word.text.lower() in word_frequencies.keys():
                
                if sent not in sentence_scores.keys():
                    
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary =' '.join(final_summary)
    return summary
        


d = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/"
file_path = os.listdir(d)[0]
file_path = d+file_path
str = convert_pdf_to_txt(file_path) 
final_summary = preprocessing(str)
print(final_summary)

if(os.path.exists("C:/xampp/htdocs/BE_Project/BE_Project/summary.txt")):
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/summary.txt', 'r+')
    outfile.truncate(0)
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/summary.txt','w',encoding="utf-8")
    outfile.write(final_summary)
else:
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/summary.txt','w',encoding="utf-8")
    outfile.write(final_summary)
outfile.close

#print("Summarization done..")