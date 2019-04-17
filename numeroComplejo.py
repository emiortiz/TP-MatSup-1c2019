import math
from decimal import Decimal

class NumeroComplejo(object):

    def __init__(self, real, imaginario):
        real = real.replace(",",".")
        imaginario = imaginario.replace(",",".")

        self.real = Decimal(real)
        self.imaginario = Decimal(imaginario)

    def getFormaBinomica(self):
        text = ''
        if self.real != 0:
            text += str(self.real)
        if self.imaginario != 0:
            if self.imaginario < 0:
                text += str(self.imaginario) + "j"
            else:
                if text != '':
                    text += "+"
                text += str(self.imaginario) + "j"
        return text

    def getFormaOrdenada(self):
        text = '('

        if self.real != 0:
            text += str(self.real)
        else:
            text += '0'

        text += ','

        if self.imaginario != 0:
            text += str(self.imaginario)
        else:
            text += '0'

        text += ')'

        return text

    def getFormaPolar(self):
        p = math.sqrt(pow(self.real,2) + pow(self.imaginario,2))

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

        return ("[" + str(round(p,2)) + "," + str(round(O,2)) + "]")

    def setEnPolar(self,p,O):
        p = p.replace(",",".")
        O = O.replace(",",".")
        a = Decimal(p) * Decimal(math.cos(Decimal(O)))
        b = Decimal(p) * Decimal(math.sin(Decimal(O)))
        self.real = round(a,4)
        self.imaginario = round(b,4)
