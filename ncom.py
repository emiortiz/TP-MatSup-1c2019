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

    numeroC = None;

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.getBinomica.clicked.connect(self.getNumero)

    def getNumero(self):
        real, okPressed = QInputDialog.getText(self, "Valor Real","Real:", QLineEdit.Normal, "")
        if okPressed and real != '':
            imag, okPressed2 = QInputDialog.getText(self, "Valor Imaginario","Imaginario:", QLineEdit.Normal, "")
            if okPressed2 and imag != '':
#               binomica = real + "+" + imag + "j"
#               ordenado = "(" + real + "+" + imag + ")"
#               self.binomicaText.setText(binomica)
#               self.ordenadoText.setText(ordenado)
                numeroC = NumeroComplejo(real,imag)
        self.binomicaText.setText(numeroC.getFormaBinomica())
        self.ordenadoText.setText(numeroC.getFormaOrdenada())
        self.polarText.setText(numeroC.getFormaPolar())

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
