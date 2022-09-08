from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/ui_receitas.ui'



class UiReceitas(QWidget):
    def __init__(self):
        super(UiReceitas,self).__init__()
        uic.loadUi(FILE_UI,self)
