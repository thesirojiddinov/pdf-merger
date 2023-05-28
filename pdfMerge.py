import PyPDF2 as pdf
import sys
import os

merger = pdf.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):        
        merger.append(file)

    merger.write("combined.pdf")    