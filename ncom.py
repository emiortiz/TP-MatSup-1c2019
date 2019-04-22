#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from numeroComplejo import NumeroComplejo
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox
from decimal import Decimal

qtCreatorFile = "ncom.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.getComplejos.clicked.connect(self.getNumerosComplejo)

        global numeroC

    # def getNumeroBinomica(self):
    #     real, okPressed = QInputDialog.getText(self, "Valor Real","Real:", QLineEdit.Normal, "")
    #     if okPressed and real != '':
    #         imag, okPressed2 = QInputDialog.getText(self, "Valor Imaginario","Imaginario:", QLineEdit.Normal, "")
    #         if okPressed2 and imag != '':
    #             try:
    #                 numeroC = NumeroComplejo(real,imag)
    #                 self.binomicaText.setText(numeroC.getFormaBinomica())
    #                 self.ordenadoText.setText(numeroC.getFormaOrdenada())
    #                 self.polarText.setText(numeroC.getFormaPolar())
    #             except:
    #                 msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")
    #
    # def getNumeroPolar(self):
    #     p, okPressed = QInputDialog.getText(self, "Modulo","Fi (p):", QLineEdit.Normal, "")
    #     if okPressed and p != '':
    #         O, okPressed2 = QInputDialog.getText(self, "Angulo","Tita en radianes (O):", QLineEdit.Normal, "")
    #         if okPressed2 and O != '':
    #
    #             try:
    #                 numeroC = NumeroComplejo("0","0")
    #                 numeroC.setEnPolar(p,O)
    #                 self.binomicaText.setText(numeroC.getFormaBinomica())
    #                 self.ordenadoText.setText(numeroC.getFormaOrdenada())
    #                 self.polarText.setText(numeroC.getFormaPolar())
    #             except:
    #                 msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def getNumerosComplejo(self,numero):

        numeroComplejo, okPressed = QInputDialog.getText(self, "Numero Complejo","Numero:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo != '':
            numeroC = self.setNumeroComplejo(numeroComplejo)
            try:
                self.binomicaText.setText(numeroC.getFormaBinomica())
                self.ordenadoText.setText(numeroC.getFormaOrdenada())
                self.polarText.setText(numeroC.getFormaPolar())
            except:
                msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")


    def setNumeroComplejo(self, numero):
        true = 1
        false = 0

        numeroComplejo = NumeroComplejo('0','0')

        if re.match('-?([0-9]+|[0-9]+\.[0-9]+)\+-?([0-9]+|[0-9]+\.[0-9]+)j', numero):
            real = numero[0:numero.find('+')]
            imaginario = numero[numero.find('+') + 1: len(numero)-1]
            numeroComplejo = NumeroComplejo(real,imaginario)
        else:
            if re.match('\[-?([0-9]+|[0-9]+\.[0-9]+),-?([0-9]+|[0-9]+\.[0-9]+)\]', numero):
                P = numero[1:numero.find(',')]
                Q = numero[numero.find(',') + 1: len(numero)-1]
                numeroComplejo.setEnPolar(P,Q)
            else:
                if re.match('\(-?([0-9]+|[0-9]+\.[0-9]+),-?([0-9]+|[0-9]+\.[0-9]+)\)', numero):
                    real = numero[1:numero.find(',')]
                    imaginario = numero[numero.find(',') + 1: len(numero)-1]
                    numeroComplejo = NumeroComplejo(real,imaginario)
                else:
                    numeroComplejo = ''

        return numeroComplejo


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
