import PyPDF2

def merge(files):
    pdfWriter = PyPDF2.PdfFileWriter()
    for pdf in files:
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for page in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(page))
    pdfOutput = open('output.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

def rotate(pdf, degree):
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNo in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNo)
        page.rotateClockwise(degree)
        pdfWriter.addPage(page)
    pdfOutput = open('output.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

def watermark(pdf, watermark_file, typ):
    pdfReader = PyPDF2.PdfFileReader(pdf)
    watermarkReader = PyPDF2.PdfFileReader(watermark_file)
    pdfWriter = PyPDF2.PdfFileWriter()
    pageObj = watermarkReader.getPage(0)
    if typ == 'first':
        page = pdfReader.getPage(0)
        page.mergePage(pageObj)
        pdfWriter.addPage(page)
        for pageNo in range(1, pdfReader.getNumPages()):
            pdfWriter.addPage(pdfReader.getPage(pageNo))
    elif typ == 'all':
        for pageNo in range(pdfReader.getNumPages()):
            page = pdfReader.getPage(pageNo)
            page.mergePage(pageObj)
            pdfWriter.addPage(page)
    pdfOutput = open('output.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
