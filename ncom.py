#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import math
from numeroComplejo import NumeroComplejo
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox
from decimal import Decimal

qtCreatorFile = "ncom.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class NCom(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.getComplejos.clicked.connect(self.getNumerosComplejo)
        self.sumarButton.clicked.connect(self.sumar)
        self.restarButton.clicked.connect(self.restar)
        self.multiplicarButton.clicked.connect(self.multiplicar)
        self.dividirButton.clicked.connect(self.dividir)
        self.potenciaButton.clicked.connect(self.potenciar)
        self.raizButton.clicked.connect(self.raiz)
        self.nesimasButton.clicked.connect(self.nesimas)
        self.fasoresButton.clicked.connect(self.sumaFasores)
        global numeroC

    def mostrarResultado(self,numeroC):
        self.binomicaText.setText(numeroC.getFormaBinomica())
        self.ordenadoText.setText(numeroC.getFormaOrdenada())
        self.polarText.setText(numeroC.getFormaPolar())

    def getNumerosComplejo(self,numero):
        numeroComplejo, okPressed = QInputDialog.getText(self, "Numero Complejo","Numero:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo != '':
            numeroC = self.setNumeroComplejo(numeroComplejo)
            try:
                self.mostrarResultado(numeroC)
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
            if re.match('\[([0-9]+|[0-9]+\.[0-9]+);-?([0-9]+|[0-9]+\.[0-9]+)\]', numero):
                P = numero[1:numero.find(';')]
                Q = numero[numero.find(';') + 1: len(numero)-1]
                numeroComplejo.setEnPolar(P,Q)
            else:
                if re.match('\(-?([0-9]+|[0-9]+\.[0-9]+),-?([0-9]+|[0-9]+\.[0-9]+)\)', numero):
                    real = numero[1:numero.find(',')]
                    imaginario = numero[numero.find(',') + 1: len(numero)-1]
                    numeroComplejo = NumeroComplejo(real,imaginario)
                else:
                    if re.match('([0-9]+|[0-9]+\.[0-9]+)?cos\(([0-9]+|[0-9]+\.[0-9]+)t((\+|-)([0-9]+|[0-9]+\.[0-9]+))?\)', numero):
                        P = numero[0:numero.find('cos')]
                        if P == '':
                            P = '1'
                        W = numero[numero.find('(') + 1 : numero.find('t')]
                        Q = numero[numero.find('t') + 1 : numero.find(')')]
                        if Q == '':
                            Q = '0'
                        numeroComplejo.setEnTrigonometrica(P,Q,W,1)
                    else:
                        if re.match('([0-9]+|[0-9]+\.[0-9]+)?sen\(([0-9]+|[0-9]+\.[0-9]+)t((\+|-)([0-9]+|[0-9]+\.[0-9]+))?\)', numero):
                            P = numero[0:numero.find('sen')]
                            if P == '':
                                P = '1'
                            W = numero[numero.find('(') + 1 : numero.find('t')]
                            Q = numero[numero.find('t') + 1 : numero.find(')')]
                            if Q == '':
                                Q = '0'
                            numeroComplejo.setEnTrigonometrica(P,Q,W,0)
                        else:
                            numeroComplejo = ''
        return numeroComplejo

    def sumar(self):
        numeroComplejo1, okPressed = QInputDialog.getText(self, "Suma","Numero 1:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo1 != '':
            numero1 = self.setNumeroComplejo(numeroComplejo1)
            numeroComplejo2, okPressed = QInputDialog.getText(self, "Suma","Numero 2:", QLineEdit.Normal, "")

            if okPressed and numeroComplejo2 != '':
                numero2 = self.setNumeroComplejo(numeroComplejo2)
                try:
                    numeroResultado = self.operacionSumar(numero1,numero2)
                    self.mostrarResultado(numeroResultado)
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def restar(self):
        numeroComplejo1, okPressed = QInputDialog.getText(self, "Resta","Numero 1:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo1 != '':
            numero1 = self.setNumeroComplejo(numeroComplejo1)
            numeroComplejo2, okPressed = QInputDialog.getText(self, "Resta","Numero 2:", QLineEdit.Normal, "")

            if okPressed and numeroComplejo2 != '':
                numero2 = self.setNumeroComplejo(numeroComplejo2)
                # try:
                numeroResultado = self.operacionRestar(numero1,numero2)
                self.mostrarResultado(numeroResultado)
                # except:
                    # msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def multiplicar(self):
        numeroComplejo1, okPressed = QInputDialog.getText(self, "Resta","Numero 1:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo1 != '':
            numero1 = self.setNumeroComplejo(numeroComplejo1)
            numeroComplejo2, okPressed = QInputDialog.getText(self, "Resta","Numero 2:", QLineEdit.Normal, "")

            if okPressed and numeroComplejo2 != '':
                numero2 = self.setNumeroComplejo(numeroComplejo2)
                try:
                    numeroResultado = self.operacionMultiplicar(numero1,numero2)
                    self.mostrarResultado(numeroResultado)
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def dividir(self):
        numeroComplejo1, okPressed = QInputDialog.getText(self, "Resta","Numero 1:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo1 != '':
            numero1 = self.setNumeroComplejo(numeroComplejo1)
            numeroComplejo2, okPressed = QInputDialog.getText(self, "Resta","Numero 2:", QLineEdit.Normal, "")

            if okPressed and numeroComplejo2 != '':
                numero2 = self.setNumeroComplejo(numeroComplejo2)
                try:
                    numeroResultado = self.operacionDividir(numero1,numero2)
                    self.mostrarResultado(numeroResultado)
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def operacionSumar(self,numero1,numero2):
        real = Decimal(numero1.getReal()) + Decimal(numero2.getReal())
        imaginario = Decimal(numero1.getImaginario()) + Decimal(numero2.getImaginario())
        numeroResultado = NumeroComplejo(str(real),str(imaginario))
        return numeroResultado

    def operacionRestar(self,numero1,numero2):
        real = Decimal(numero1.getReal()) - Decimal(numero2.getReal())
        imaginario = Decimal(numero1.getImaginario()) - Decimal(numero2.getImaginario())
        numeroResultado = NumeroComplejo(str(real),str(imaginario))
        return numeroResultado

    def operacionMultiplicar(self,numero1,numero2):
        real = Decimal(numero1.getReal()) * Decimal(numero2.getReal()) + (-1) * Decimal(numero1.getImaginario()) * Decimal(numero2.getImaginario())
        imaginario = Decimal(numero1.getReal()) * Decimal(numero2.getImaginario()) + Decimal(numero1.getImaginario()) * Decimal(numero2.getReal())
        numeroResultado = NumeroComplejo(str(real),str(imaginario))
        return numeroResultado

    def operacionDividir(self,numero1,numero2):
        conjugadoDivisor = self.getConjugado(numero2)
        divisorResultado = math.pow(Decimal(numero2.getReal()),2) + math.pow(Decimal(numero2.getImaginario()),2)
        dividendo = self.operacionMultiplicar(numero1,conjugadoDivisor)
        parteReal = Decimal(dividendo.getReal()) / Decimal(divisorResultado)
        parteImaginaria = Decimal(dividendo.getImaginario()) / Decimal(divisorResultado)
        numeroResultado = NumeroComplejo(str(round(parteReal,2)),str(round(parteImaginaria,2)))
        return numeroResultado

    def getConjugado(self,numero):
        real = numero.getReal()
        imaginario = Decimal(numero.getImaginario()) * (-1)
        conjugado = NumeroComplejo(str(real),str(imaginario))
        return conjugado

    def operacionPotencia(self,numero,exponente):
        nuevoModulo = math.pow(Decimal(numero.getModulo()),Decimal(exponente))
        nuevoAngulo = Decimal(numero.getAngulo()) * Decimal(exponente)
        numeroResultado = NumeroComplejo('0','0')
        numeroResultado.setEnPolar(str(nuevoModulo),str(nuevoAngulo))
        return numeroResultado

    def potenciar(self):
        numeroComplejo, okPressed = QInputDialog.getText(self, "Potencia","Complejo:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo != '':
            numero = self.setNumeroComplejo(numeroComplejo)
            exponente, okPressed = QInputDialog.getText(self, "Potencia","Exponente::", QLineEdit.Normal, "")

            if okPressed and exponente != '':
                try:
                    numeroResultado = self.operacionPotencia(numero,exponente)
                    self.mostrarResultado(numeroResultado)
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def operacionRaiz(self,numero,raiz):
        nuevoModulo = math.pow(Decimal(numero.getModulo()),(1/Decimal(raiz)))
        nuevoAngulo = Decimal(numero.getAngulo()) / Decimal(raiz)
        numeroResultado = NumeroComplejo('0','0')
        numeroResultado.setEnPolar(str(round(nuevoModulo,2)),str(round(nuevoAngulo,2)))
        return numeroResultado

    def raiz(self):
        numeroComplejo, okPressed = QInputDialog.getText(self, "Raiz","Complejo:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo != '':
            numero = self.setNumeroComplejo(numeroComplejo)
            raiz, okPressed = QInputDialog.getText(self, "Raiz","Raiz:", QLineEdit.Normal, "")

            if okPressed and raiz != '':
                try:
                    numeroResultado = self.operacionRaiz(numero,raiz)
                    self.mostrarResultado(numeroResultado)
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def nesimas(self):
        numero = NumeroComplejo('0','0')
        numeroComplejo, okPressed = QInputDialog.getText(self, "Raiz","Complejo:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo != '':
            numero = self.setNumeroComplejo(numeroComplejo)
            raiz, okPressed = QInputDialog.getText(self, "Raiz","Raiz:", QLineEdit.Normal, "")

            if okPressed and raiz != '':
                try:
                    nuevoModulo = math.pow(Decimal(numero.getModulo()),(1/Decimal(raiz)))

                    raices = []

                    for k in range (0,int(raiz)):
                        nuevoAngulo = (Decimal(numero.getAngulo()) + 2 * k * Decimal(math.pi)) / Decimal(raiz)
                        nuevaRaiz = "[" + str(round(nuevoModulo,2)) + ";" + str(round(nuevoAngulo,2)) + "]"

                        #if k != (int(raiz)-1):
                        #    nuevaRaiz += " - "

                        raices.append(nuevaRaiz)

                    raicesEnTexto = ""

                    for i in range(len(raices)):
                        raicesEnTexto += "W" + str(i) + " = " + raices[i]
                        raicesEnTexto += "\n"

                    msgBox = QMessageBox()

                    msgBox.setWindowTitle("MessageBox demo")
                    msgBox.setText(raicesEnTexto)

                    msgBox.exec()

                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

    def sumaFasores(self):
        numero1 = NumeroComplejo('0','0')
        numero2 = NumeroComplejo('0','0')
        numeroComplejo1, okPressed = QInputDialog.getText(self, "Suma de fasores","Numero 1:", QLineEdit.Normal, "")
        if okPressed and numeroComplejo1 != '':
            numero1 = self.setNumeroComplejo(numeroComplejo1)
            numeroComplejo2, okPressed = QInputDialog.getText(self, "Suma de fasores","Numero 2:", QLineEdit.Normal, "")

            if okPressed and numeroComplejo2 != '':
                numero2 = self.setNumeroComplejo(numeroComplejo2)
                try:
                    if numero1.getFrecuencia() == numero2.getFrecuencia() :
                        real = numero1.getReal() + numero2.getReal()
                        imaginario = numero1.getImaginario() + numero2.getImaginario()
                        numeroFinal = NumeroComplejo(str(real),str(imaginario))
                        numeroFinal.setFrecuencia(numero1.getFrecuencia())

                        msgBox = QMessageBox(self)
                        msgBox.setWindowTitle("Suma")
                        msgBox.setText(numeroFinal.getFormaTrigonometrica())
                        msgBox.exec()
                    else:
                        msgBox = QMessageBox.critical(self,"Datos incorrectos","Frecuencias distintas, no se puede realizar la suma")
                except:
                    msgBox = QMessageBox.critical(self,"Datos incorrectos","Vuelva a intentarlo")

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = NCom()
    window.show()
    sys.exit(app.exec_())
