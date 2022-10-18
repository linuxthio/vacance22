

#!/usr/bin/python

# code generer par :djibysoft

from PySide2.QtWidgets import QApplication,QMainWindow,QHBoxLayout, QHBoxLayout,QPushButton,QTextEdit, QLineEdit, QVBoxLayout, QWidget, QRadioButton, QButtonGroup

import os, sys
import wget
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class Fen(QMainWindow):
    def __init__(self):
        super(Fen, self).__init__()
        self.setWindowTitle("ex1")
        self.setGeometry(200, 200, 300, 250)
        self.setFixedSize(300, 200)
        self.b = QPushButton("Allez les bott! ")
        self.centralWidget=QWidget(self)
        self.lay=QVBoxLayout(self)
        self.centralWidget.setLayout(self.lay)
        self.lay.addWidget(self.b)
        self.b.setFixedWidth(400)
        self.b.setStyleSheet("color:red;font-size:32px;")



        
        


a = QApplication(sys.argv)
f = Fen()

f.show()
a.exec_()
   
    