import PyPDF2
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import os
from heapq import nlargest
import string
from string import punctuation


def text_extract(file_path):
    #fileobj=open(file_path,"rb")
    pdfreader=PyPDF2.PdfFileReader(file_path)
    num_of_pages=pdfreader.numPages
    article=""
    for i in range(num_of_pages):
        article+=pdfreader.getPage(i).extractText()
    print(article)  
    print("End of text")     
    print()
    print()
    with open("C:/xampp/htdocs/BE_Project/BE_Project/test.txt","w")as f:
        f.write(article)
        article=article.replace("\n","")
        #article=article.replace(" ","")
        article=article.rstrip()
        
def text_clean(file_path):
    with open(file_path, 'r') as f:
        lines = f.read()
    # remove spaces
    lines = [line.replace('\n', '') for line in lines]
    # finally, write lines in the file
    with open(file_path, 'w') as f:
        f.writelines(lines)
    with open(file_path,'r') as f:
        contents = f.read() 
    return contents       

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
    all_frequencies=word_frequencies.values()
    max_value=max(all_frequencies)
    for word in word_frequencies:
        word_frequencies[word]=word_frequencies[word]/max_value
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores={}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens)*0.4)
    summary = nlargest(select_length,sentence_scores,key=sentence_scores.get)
    final_summary= [word.text for word in summary]
    summary=' '.join(final_summary)
    return summary
        


if(os.path.exists("C:/xampp/htdocs/BE_Project/BE_Project/test.txt")):
            outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/test.txt', 'r+')
            outfile.truncate(0)


d = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/"
file_path=os.listdir(d)[0]
file_path=d+file_path
text_extract(file_path) 
file_path="C:/xampp/htdocs/BE_Project/BE_Project/test.txt"
str=text_clean(file_path)
final_summary=preprocessing(str)
#print(final_summary)


if(os.path.exists("C:/xampp/htdocs/BE_Project/BE_Project/summary.txt")):
    outfile = open("C:/xampp/htdocs/BE_Projects/BE_Project/summary.txt", 'r+')
    outfile.truncate(0)
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/summary.txt','w')
    outfile.write(final_summary)
else:
    outfile = open('C:/xampp/htdocs/BE_Project/BE_Project/summary.txt','w')
    outfile.write(final_summary)
outfile.close
'''for f in os.listdir(d):
    os.remove(os.path.join(d, f))
 '''
print("Summarization Done Sucessfully...")


'''$command_exec = escapeshellcmd('python F:\Python_projects\Text_Summarization.py');
$str_output = shell_exec($command_exec);
echo $str_output;
'''