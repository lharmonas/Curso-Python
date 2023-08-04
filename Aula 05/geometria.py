class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area (self):
        return(self.altura * self.base)
    
    def perimetro (self):
        return (2*(self.base+self.altura))