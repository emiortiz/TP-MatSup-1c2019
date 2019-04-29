import unittest
import sys
from numeroComplejo import NumeroComplejo
from ncom import NCom
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox

class NumerosComplejosTest(unittest.TestCase):

    def testBinomicaAPolarPositivoPositivo(self):
        numero = NumeroComplejo("3","5")
        self.assertEqual(numero.getFormaPolar(),"[5.83;1.03]")

    def testBinomicaAPolarPositivoNegativo(self):
        numero = NumeroComplejo("3","-5")
        self.assertEqual(numero.getFormaPolar(),"[5.83;5.25]")

    def testBinomicaAPolarNegativoPositivo(self):
        numero = NumeroComplejo("-3","5")
        self.assertEqual(numero.getFormaPolar(),"[5.83;2.11]")

    def testBinomicaAPolarNegativoNegativo(self):
        numero = NumeroComplejo("-3","-5")
        self.assertEqual(numero.getFormaPolar(),"[5.83;4.17]")

    def testSetNumeroEnOrdenada(self):
        numeroStr = "(3,5)"
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        numeroComp = main.setNumeroComplejo(numeroStr)
        self.assertEqual(numeroComp.getFormaPolar(),"[5.83;1.03]")

    def testSetNumeroEnPolar(self):
        numeroStr = "[5.83;4.17]"
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        numeroComp = main.setNumeroComplejo(numeroStr)
        self.assertEqual(numeroComp.getFormaOrdenada(),"(-3.01,-4.99)")

    def testSumar(self):
        numero1 = NumeroComplejo("3","5")
        numero2 = NumeroComplejo("4","-3")
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        resultado = main.operacionSumar(numero1,numero2)
        self.assertEqual(resultado.getFormaOrdenada(),"(7,2)")

    def testRestar(self):
        numero1 = NumeroComplejo("3","5")
        numero2 = NumeroComplejo("4","-3")
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        resultado = main.operacionRestar(numero1,numero2)
        self.assertEqual(resultado.getFormaOrdenada(),"(-1,8)")

    def testMultiplicar(self):
        numero1 = NumeroComplejo("4","5")
        numero2 = NumeroComplejo("3","-5")
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        resultado = main.operacionMultiplicar(numero1,numero2)
        self.assertEqual(resultado.getFormaOrdenada(),"(37,-5)")

    def testMultiplicar(self):
        numero1 = NumeroComplejo("3","4")
        numero2 = NumeroComplejo("2","1")
        app = QtWidgets.QApplication(sys.argv)
        main = NCom()
        resultado = main.operacionDividir(numero1,numero2)
        self.assertEqual(resultado.getFormaOrdenada(),"(2.00,1.00)")
