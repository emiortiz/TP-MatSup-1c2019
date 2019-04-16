import math
from decimal import Decimal

class NumeroComplejo(object):
    
    def __init__(self, real, imaginario):
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
        O = math.atan(self.imaginario/self.real)
        return (str(round(p,2)) + '(' + str(round(math.cos(O),2)) + '+' + str(round(math.sin(O),2)) + 'j')
