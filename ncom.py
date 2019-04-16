#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from numeroComplejo import NumeroComplejo
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from decimal import Decimal

qtCreatorFile = "ncom.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.getBinomica.clicked.connect(self.getNumeroBinomica)
        self.getPolar.clicked.connect(self.getNumeroPolar)

        global numeroC

    def getNumeroBinomica(self):
        real, okPressed = QInputDialog.getText(self, "Valor Real","Real:", QLineEdit.Normal, "")
        if okPressed and real != '':
            imag, okPressed2 = QInputDialog.getText(self, "Valor Imaginario","Imaginario:", QLineEdit.Normal, "")
            if okPressed2 and imag != '':
                numeroC = NumeroComplejo(real,imag)
        self.binomicaText.setText(numeroC.getFormaBinomica())
        self.ordenadoText.setText(numeroC.getFormaOrdenada())
        self.polarText.setText(numeroC.getFormaPolar())


    def getNumeroPolar(self):
        p, okPressed = QInputDialog.getText(self, "Modulo","Fi (p):", QLineEdit.Normal, "")
        if okPressed and p != '':
            O, okPressed2 = QInputDialog.getText(self, "Angulo","Tita en radianes (O):", QLineEdit.Normal, "")
            if okPressed2 and O != '':
                #CALCULOS PARA SACAR LA FORMA BINOMICA
                numeroC = NumeroComplejo(0,0)
                numeroC.setEnPolar(p,O)
        self.binomicaText.setText(numeroC.getFormaBinomica())
        self.ordenadoText.setText(numeroC.getFormaOrdenada())
        self.polarText.setText(numeroC.getFormaPolar())


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
