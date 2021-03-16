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

def rotate(file, degree):
    pdfReader = PyPDF2.PdfFileReader(file)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNo in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNo)
        page.rotateClockwise(degree)
        pdfWriter.addPage(page)
    pdfOutput = open('output.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()