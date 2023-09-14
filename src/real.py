
class Real:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        if self.value > 0 or self.value < 0:
            return f'{self.value}'
        return ''
    
    def get_value(self):
        return self.value
    
    def __add__(self, other):
        return Real(self.value + other.get_value())
    
    def __sub__(self, other):
        return Real(self.value - other.get_value())
    
    def __mul__(self, other):
        return Real(self.value * other.get_value())
