import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
reader = pyPDF2.PdfFileReader(book)
pages = reader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()














