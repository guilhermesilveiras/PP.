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

    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Triangulo(Forma):

    def __init__(self, ladoA, ladoB, ladoC, altura):
        super().__init__()
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.altura = altura

    def calcPerimetro(self):
        self.perimetro = self.ladoA + self.ladoB + self.ladoC
        return self.perimetro

    def calcArea(self):
        self.area = (self.ladoB*self.altura)/2
        return self.area

class Retangulo(Forma):

    def __init__(self, ladoA, ladoB):
        Forma.__init__(self)
        self.ladoA = ladoA
        self.ladoB = ladoB

    def calcPerimetro(self):
        self.perimetro = self.ladoA*2 + self.ladoB*2
        return self.perimetro

    def calcArea(self):
        self.area = self.ladoA * self.ladoB
        return self.area

t1 = Triangulo(2, 3, 4, 5)
x = t1.calcPerimetro()
print(x)
x = t1.calcArea()
print(x)
r1 = Retangulo(2, 4)
y = r1.calcPerimetro()
print(y)
y = r1.calcArea()
print(y)

print(isinstance(t1, Forma))
print(isinstance(r1, Forma))
