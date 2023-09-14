from real import Real
from imag import Imag

class Complex:
    def __init__(self, real, imag):
        self.__real = Real(real)
        self.__imag = Imag(imag)
    
    def __str__(self):
        return f'{self.__real}{self.__imag}'
    
    def get_real(self):
        return self.__real
    
    def get_imag(self):
        return self.__imag
    
    def get_value(self):
        return (self.__real.get_value(), self.__imag.get_value())
    

    def __add__(self, other):
        return Complex(
                       (self.__real + other.get_real()).get_value(),
                       (self.__imag + other.get_imag()).get_value()
                      )
    
    def __sub__(self, other):
        return Complex(
                       (self.__real - other.get_real()).get_value(),
                       (self.__imag - other.get_imag()).get_value()
                      )
    
    def __mul__(self, other): # (r1 + i1) * (r2 + i2) = r1*r2 + r1*i2 + i1*r2 + i1*i2 = (r1*r2 - i1*i2) + (r1*i2 + i1*r2)
        return Complex(
                       ( (self.__real * other.get_real()) - (self.__imag * other.get_imag()) ).get_value(),
                       ( (self.__real * other.get_imag()) + (self.__imag * other.get_real()) ).get_value()
                      )
    
    # hello