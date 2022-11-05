import operator
import argparse, sys
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
#sys.path.append("C:/Users/kukad/LEARNING-BASED-AUTOMATIC-PPT-GENERATION/")
sys.path.append("../..")
from BulletIdentifier import BulletIdentifier as bi
from FeatureExtractor import FeatureExtractor as fe
from SlideGenerator1 import SlideGenerator1 as sg
import os
import time
from PdftoText import PdftoText as p2t


class Driver:
    def __init__(self):
        pass

    def listToString(s):  
        str1= " "   
        return (str1.join(s)) 
        
    def get_threshold(self, featureValuesDict):
        featureValues = list(featureValuesDict.values())
        return sum(featureValues) / float(len(featureValues))

    def read_sentences(self, filepath, chunk_size = 10240):
        last = ""
        with open(filepath) as inp:
            while True:
                buf = inp.read(chunk_size)
                buf = ''.join([i if ord(i) < 128 else ' ' for i in buf])
                if not buf:
                    break
                sentences = sent_tokenize(last + buf)
                last = sentences.pop()
                for sentence in sentences:
                    yield sentence.replace('\n', ' ')
            yield last.replace('\n', ' ')

    def get_sentences(self, file_name):
        valid_sentences = []
        for sentence in self.read_sentences(file_name):
            num_words = len(word_tokenize(sentence))
            if num_words in range(2, 30):
                valid_sentences.append(sentence)
        return valid_sentences

    def driver(self, filepath, title):	
        weights = {'SWP': 0.1, 'NOWT': 0.5, 'NNP': 0.3, 'NVP': 0.1}

        SWPValues = {}
        NOWTValues = {}
        NNPValues = {}
        NVPValues = {}

        currentSent = 1
        sentences = []
        valid_sentences = self.get_sentences(filepath) 
        # sentences with word count in range(2,30)
        for sentence in valid_sentences:
            sentences.append(sentence)
            tokenArray = word_tokenize(sentence)
            if len(tokenArray) > 2:
                SWPValues[currentSent] = fe().getStopWordsPerc(tokenArray)
                NOWTValues[currentSent] = fe().getNumOverlappingWords(title, sentence)
                NNPValues[currentSent] = fe().getNumNounPhrases(tokenArray)
                NVPValues[currentSent] = fe().getNumVerbPhrases(tokenArray)
                currentSent += 1

        totalSent = currentSent
        LinesScore = {}
        for sent_num in range(1, totalSent - 1):
            score = ((SWPValues[sent_num] * weights['SWP']) + (NOWTValues[sent_num] * weights['NOWT']) + (NNPValues[sent_num] * weights['NNP']) + (NVPValues[sent_num] * weights['NNP']))
            LinesScore[sent_num] = (score, sentences[sent_num])
        print ("LineScore ",LinesScore)
        sortedSentDict = sorted(LinesScore.items(), key=operator.itemgetter(1), reverse=True)
        return sortedSentDict

    def extract_sent_from_dict(self, sortedSentDict, topSentRatio=0.4):
        filteredSentDict = dict(sortedSentDict[:int(len(sortedSentDict) * topSentRatio)])
        sortedSentDict = sorted(filteredSentDict.items())  # sorted by occurance
        output = []
        for k, v in sortedSentDict:
            sent = v[1]
            output.append((k, sent))
	    #print "extract_sent_from_dict ",output
        return output
               

if __name__ == '__main__':
    '''
        6 args
        1. text_file_path
        2. Title
        3. Subtitle
        4. output PPTX file name
        5. footer
        6. logo
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument("-O", "--outputfile", required=True, help="Name of the output file")
    ap.add_argument("-P", "--processStatusFile", required=True, help="Proceess status",default='logo.png')
    ap.add_argument("-T", "--title", required=False, help="PPTX Title")
    ap.add_argument("-I", "--inputfile", required=False, help="Path to the input file")
    ap.add_argument("-S", "--subtitle", required=False, help="PPTX SubTitle", default='')
    ap.add_argument("-F", "--footer", required=False, help="PPTX Footer", default='')
    ap.add_argument("-L", "--logo", required=False, help="PPTX logo", default='logo.png')
    args = vars(ap.parse_args())

    output_file_name = args['outputfile']
    process_status_file = args['processStatusFile']
    ppt_title = args['title']
    ppt_sub_title = args['subtitle']
    ppt_footer = args['footer']
    ppt_logo = args['logo']

    bi = bi()   
    #print("bi")
    sg = sg()
    #print("sg")
    p2t = p2t()
    #print("p2d")
    d = Driver()
    #print("d")

    d9 = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/"
    file_path = os.listdir(d9)[0]
    #file_path=d+file_path
    input_file_path0 = d9+file_path

    #print("uploaded input file 1")

    output = p2t.convert_pdf_to_txt(input_file_path0)
    print(output)
    opath = "C:/xampp/htdocs/BE_Project/BE_Project/outputText.txt"
    f = open(opath, "w")
    f.write(output)
    
    input_file_path = "C:/xampp/htdocs/BE_Project/BE_Project/outputText.txt"

    #print("uploaded input file 3")

    d2 = "C:/xampp/htdocs/BE_Project/BE_Project/titlefile.txt"
    with open(d2) as f:
        lines = f.read()
    ppt_title = lines
    print(ppt_title)

    #print("uploaded input file 4")

    #ppt_title = d.listToString(lines)
    #print(ppt_title)

    sortedSentDict = d.driver(input_file_path, ppt_title)
    sent_dict = dict(d.extract_sent_from_dict(sortedSentDict))
    important_sent_num = sent_dict.keys()
    sent_num_list = list(important_sent_num)
    sentences, bullet_map = bi.identify_bullet_sentences(input_file_path)
    all_bullet_sentence_nos = []
    for bullet_data in bullet_map.values():
        all_bullet_sentence_nos.append(bullet_data)

    #print("uploaded input file 5")

    for sent_num in important_sent_num:
        for bullet_list in all_bullet_sentence_nos:
            if sent_num in bullet_list:
                sent_num_list.extend(bullet_list)
                break

    #print("uploaded input file 6")

    with open(process_status_file, "w", encoding="UTF-8") as fp:
        fp.write("st2")

    time.sleep(2)

    #print("uploaded input file 7")

    sent_num_list = sorted(set(sent_num_list))
    sent_list = []
    for num in sent_num_list:
        print (num, sentences[num])
        sent_list.append(sentences[num])

    #print("uploaded input file 8")

    sg.create_presentation(output_file_name, ppt_title, ppt_sub_title, sent_list)
    print (sent_list)
    with open(process_status_file, "w") as fp:
        fp.write("st3")

    #print("uploaded input file 9")
    #os.system("rm -f outputs/slides-archive/*.txt")