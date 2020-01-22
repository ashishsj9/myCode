import os
import sys

from pdf2image import convert_from_path

def convertPDF(pdf_file):
    try:
        if pdf_file.endswith(".pdf"):
            pages = convert_from_path(pdf_file, 300)
            pdf_file = pdf_file[:-4]
            for page in pages:
                page.save("%s-page%d.jpeg" % (pdf_file,pages.index(page)+1), "JPEG")
            return("Success")
        else:
            return("Given input is not an pdf")
    except PDFPageCountError as error:
        print("unable to convert pdf to image"+error)
         
convertPDF("/Users/ashishjhade/Desktop/Profile.pdf")