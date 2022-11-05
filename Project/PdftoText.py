import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

class PdftoText:
    def __init__(self):
        pass

    def convert_pdf_to_txt(self, path):
        #print("Format not supported!")
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
        sentence = text.replace('',' ')
        retstr.close()
        return sentence
'''
    d = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/"
    file_path = os.listdir(d)[0]
    #file_path=d+file_path
    input_file_path0 = d+file_path
    convert_pdf_to_txt(input_file_path0)
'''
