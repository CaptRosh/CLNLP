import os
from PyPDF2 import PdfFileMerger

for i in range(1,9):
    os.system(f"jupyter nbconvert --to pdf ../exp{i}/exp{i}.ipynb")


pdfs = [f"../exp{i}/exp{i}.pdf" for i in range(1,9)]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("A060_NehaKulkarni_NLPSubmission.pdf")
merger.close()