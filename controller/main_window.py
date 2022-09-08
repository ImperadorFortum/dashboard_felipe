from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from controller.home import Home
from controller.ui_despesas import UiDespesas
from controller.ui_receitas import UiReceitas
from theme.app_theme import DARK,LIGHT


FILE_UI = 'view/MainWindow.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self)
        uic.loadUi(FILE_UI,self)
        
        #cria os objetos das páginas
        self.pagehome = Home 
        self.pagereceitas = Receitas
        self.pageDespesas = Despesas

        # Insere as páginas 
        self.stackedWidget.addWidget(self.pagehome)
        self.stackedWideget.addWidget(self.pageReceitas)
        self.stackedWidget.addWidget(self.pagedDespesas)
       
        #ações dos botões 
        self.btnHome.clicked.connect(self.actionMenu)
        self.btnReceitas.clicked.connect(self.actionMenu)
        self.btnDespesas.clicked.connect(self.actionMenu)
        self.btnDark.clicked.connect(self.actionMenu)
        self.btnLight.clicked.connect(self.actionMenu)

    def actionMenu():
        btn = self.sender()    
        nomeBtn = btn.objectname()
        if nomeBtn == 'btnHome':
            self.stackedWidget.setCurrentIndex(0)
        if nomeBtn == 'btnReceitas':   
            self.stackedWidget.setCurrentIndex(1)
        if nomeBtn == 'btnDespesas':  
            self.stackedWidget.setCurrentIndex(2)
        if nomeBtn == 'btnLight':
            self.setStyleSheet(LIGHT)

        if nomeBtn == 'btnDark':
            self.setStyleSheet(DARK)

