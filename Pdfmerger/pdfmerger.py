import PyPDF2
import sys
import os

merger = PyPDF2.PdffileMerger()

for file in os.listdir(os.curdir):
    if file.endwith("pdf"):
        merger.append(file)
    merger.write("sethfiles.pdf")
    
        

