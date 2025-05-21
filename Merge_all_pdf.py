import PyPDF2
import os

merger = PyPDF2.PdfMerger()
for pdf in os.listdir():
    if pdf.endswith(".pdf"):
        merger.append(pdf)
merger.write("merged.pdf")
merger.close()
