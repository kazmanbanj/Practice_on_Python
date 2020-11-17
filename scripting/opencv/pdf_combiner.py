import PyPDF2
import sys

inputs = sys.argv[1:]   # this will called arg 1 and all other args after it

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)





# To combine pdfs together, run: python pdf_combiner.py dummy.pdf twopage.pdf tilt.pdf