class Imag:
    def __init__(self, value, num_type='i'):
        self.__value = value
        self.num_type = num_type
    
    def __str__(self):
        if self.__value > 1 or self.__value < -1:
            if self.__value > 0:
                return f'+{self.__value}{self.num_type}'
            return f'{self.__value}{self.num_type}'
        elif self.__value == 1:
            return f'+{self.num_type}'
        elif self.__value == -1:
            return '-i'
        return ''
    

    def get_value(self):
        return self.__value
    
    
    def __add__(self, other):
        return Imag(self.__value + other.get_value())
    
    def __sub__(self, other):
        return Imag(self.__value - other.get_value())
    
    def __mul__(self, other):
        return Imag(self.__value * other.get_value())