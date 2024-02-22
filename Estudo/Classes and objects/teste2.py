# 2. Crie uma classe chamada Forma, que possui os
# atributos area e perimetro.
# – Implemente as subclasses Retangulo e Triangulo, que
# devem conter os métodos calculaArea e
# calculaPerimetro. A classe Triangulo deve ter também
# o atributo altura.
#
# • No código de teste crie um objeto da classe
# Triangulo e outro da Classe Retangulo. Verifique
# se os dois são mesmo instancias de Forma (use
# instanceof) , e calcule a área de cada um.


class Forma:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro


class Triangulo(Forma):

    def __init__(self, altura, area, perimetro):
        Forma.__init__(self, area, perimetro)
        self.altura = altura

    def calcPerimetro(self):
        return self.perimetro

    def calcArea(self):
        return self.area

class Retangulo(Forma):

    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calcPerimetro(self):
        return self.perimetro

    def calcArea(self):
        return self.area

t1 = Triangulo(10, 20, 30)
print(isinstance(t1, Forma))

r1 = Retangulo(10, 20)
print(isinstance(r1, Forma))


