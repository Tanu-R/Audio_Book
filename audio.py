#1.Install pyttsx3 and PyPDF2 in pycharm terminal#
import pyttsx3
import PyPDF2
book = open('CNN_Basic.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
