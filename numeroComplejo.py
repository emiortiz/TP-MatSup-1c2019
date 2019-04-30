import math
from decimal import Decimal

class NumeroComplejo(object):

    def __init__(self, real, imaginario):
        real = real.replace(",",".")
        imaginario = imaginario.replace(",",".")

        self.real = Decimal(real)
        self.imaginario = Decimal(imaginario)
        self.frecuencia = "23"
        self.modulo = ''
        self.angulo = ''

    def getReal(self):
        return self.real;

    def getImaginario(self):
        return self.imaginario

    def getModulo(self):
        if self.modulo == '':
            p = math.sqrt(pow(self.real,2) + pow(self.imaginario,2))
            return p
        else:
            return Decimal(self.modulo)

    def getAngulo(self):

        if self.angulo == '':

            if self.real != 0 :
                O = math.atan(self.imaginario/self.real)
            else:
                if self.imaginario > 0 :
                    O = math.pi / 2
                else:
                    O = math.pi * 3 / 2

            if (self.real > 0) and (self.imaginario < 0) :
                O += 2 * math.pi

            if self.real < 0 :
                O += math.pi

            return O
        else:
            return Decimal(self.angulo)


    def getFormaBinomica(self):
        text = ''
        if self.real != 0:
            text += str(round(self.real,2))
        if self.imaginario != 0:
            if self.imaginario < 0:
                text += str(round(self.imaginario,2)) + "j"
            else:
                if text != '':
                    text += "+"
                text += str(round(self.imaginario,2)) + "j"
        return text

    def getFormaOrdenada(self):
        text = '('

        if self.real != 0:
            text += str(round(self.real,2))
        else:
            text += '0'

        text += ','

        if self.imaginario != 0:
            text += str(round(self.imaginario,2))
        else:
            text += '0'

        text += ')'

        return text

    def getFormaPolar(self):
        return ("[" + str(round(self.getModulo(),2)) + ";" + str(round(self.getAngulo(),2)) + "]")

    def setEnPolar(self,p,O):
        p = p.replace(",",".")
        O = O.replace(",",".")
        if Decimal(O) < 0:
            O = Decimal(O) + Decimal(math.pi) * 2

        self.modulo = p
        self.angulo = O
        self.real = Decimal(p) * Decimal(math.cos(Decimal(O)))
        self.imaginario = Decimal(p) * Decimal(math.sin(Decimal(O)))

    def setFrecuencia(self,w):
        self.frecuencia = w

    def setEnTrigonometrica(self,p,O,w,cos):
        if cos != 1:
            O = Decimal(O) + Decimal(math.pi) / 2

        self.setEnPolar(p,str(O))
        self.frecuencia = w

    def getFrecuencia(self):
        return self.frecuencia

    def getFormaTrigonometrica(self):
        return (str(round(self.getModulo(),2)) + " cos(" + self.getFrecuencia() + "t + " + str(round(self.getAngulo(),2)) + ")")
