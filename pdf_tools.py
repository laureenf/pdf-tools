import PyPDF2

def merge(files):
    pdfWriter = PyPDF2.PdfFileWriter()
    for file in files:
        pdfReader = PyPDF2.PdfFileReader(file)
        for page in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(page))
    pdfOutput = open('output.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()