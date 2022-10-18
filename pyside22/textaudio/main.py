
#!/usr/bin/python
# code generer par :djibysoft
from PySide6.QtWidgets import QApplication,QHBoxLayout, QHBoxLayout,QPushButton,QTextEdit, QLineEdit, QVBoxLayout, QWidget, QRadioButton, QButtonGroup,QPlainTextEdit
import os, sys
import wget
from PySide6.QtCore import QUrl
# from PySide6.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage

from GoogleTTS import GoogleTTS

import nltk
from nltk import tokenize
nltk.download('punkt')


def decoupe(ch,n):

    p=print
    lg=len(ch.strip())

    data=[]
    part=''
    nmax=lg//n
    pd=tokenize.sent_tokenize(ch)
    p(pd)
    p('long = ',lg,' max = ',nmax,'pd = ',len(pd))
    # for i in range(0,lg,nmax):
    #     p(ch[i:i+nmax])
    #     data.append(ch[i:i+nmax])
    
    p('long = ',lg,' max = ',nmax,' long data=',len(data))
    return pd


def google_wakh(txt,lang,genre,filename,ds):
    tts = GoogleTTS()
    # print(dir(tts.tts))
    tts.set_language_code(lang)
    tts.set_ssml_gender(genre)
    print('debut ... '+ds+'/'+ filename+'.mp3')
    ret = tts.tts(txt,ds+'/'+ filename+'.mp3')
    print("fin ...")
    if 'audioContent' in ret:
        b64 = ret['audioContent']
        print(b64)
        import os
        os.system(f"vlc {filename}.mp3")
    else:
        error = ret['error']
        code = error['code']
        message = error['message']
        status = error['status']
        print(error,code,message,status)
    try:
        pass
    except :
        pass
    

def google_decoupe(txt,lang,genre,filename,user,premium=False):
    """
    . on teste la longueur de txt
    . si len(txt)> 2500 et < 5000
        - alors on decoupe en deux parties
        - si >5000 <7500
            .. on decoupe en 3 partie
            
    - on boucle sur le tableau cree pour enregistrer dans un dossier username/tmp/...
    - on merge l'ensemble des mp3 dans un fichier filename.mp3 dans le dossier media/username/
    - 

    """
    
    tab1=[]
    tab2=[]
    tab3=[]
    if len(txt)<2500:
        google_wakh(txt,lang,genre,filename,user,premium=False)
        return 'ok'
    else:
        paragraphe=decoupe(txt)
        d=len(paragraphe)

        if len(txt)>=2500 and len(txt)<5000:
            size_2=int(d/2)
            
            tab1=" ".join(paragraphe[:size_2])
            tab2=" ".join(paragraphe[size_2:])
        
            return "ok"

        elif len(txt)>=5000 and len(txt)<7500:
            size_3=int(d/3)

            tab1=" ".join(paragraphe[:size_3])
            tab2=" ".join(paragraphe[size_3:(2*size_3)])
            tab3=" ".join(paragraphe[(2*size_3):])
            
            return "ok"
        else:
            return "Error"


class Fen(QWidget):
    def __init__(self):
        super(Fen, self).__init__()
        self.setWindowTitle("web1")
        self.setGeometry(200, 200,300, 200)
        #self.setFixedSize(300, 200)
        self.vb=QVBoxLayout(self)
        self.setLayout(self.vb)
        self.b = QPushButton("Charger")
        # self.txturl=QLineEdit()   
        self.txtaudio=QPlainTextEdit()

        self.view = QWebEngineView()
        # self.vb.addWidget(self.txturl)
        self.vb.addWidget(self.b)
        self.vb.addWidget(self.txtaudio)
        self.vb.addWidget(self.view)
       
        self.url="http://djibysoft.com/"        
        self.view.load(QUrl(self.url))
        self.view.show()
        self.b.clicked.connect(self.geturl)
    def geturl(self):
        self.url=str(self.txturl.text())
        self.view.load(QUrl(self.url))
        self.view.show()
        print(self.url)
a = QApplication(sys.argv)
f = Fen()
f.show()
a.exec_()
       
    
