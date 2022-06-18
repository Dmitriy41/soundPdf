import pyttsx3
from pdfminer.high_level import extract_text
from pyfiglet import Figlet
def PdfSay(pdfFile):
    doc = extract_text(pdfFile)
    engine  = pyttsx3.init()
    engine.setProperty('volume', 0.9)
    engine.say(doc)
    engine.runAndWait()

def main():
    zastavka = Figlet()
    print(zastavka.renderText("PDF to Sound"))
    print("Введите название pdf файла который надо озвучить(без .pdf)")
    name = input()
    PdfSay(name+".pdf")

if __name__=="__main__":
    main()






