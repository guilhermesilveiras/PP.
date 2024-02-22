class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcPerimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def getmaiorlado(self):
        if self.a > self.b and self.a > self.b:
            print('O maior lado é igual a: ', self.a)
        elif self.b > self.a and self.b > self.c:
            print('O maior lado é igual a: ', self.b)
        elif self.c > self.a and self.c > self.b:
            print('O maior lado é igual a: ', self.c)
        else:
            print('Não foi impossível encontrar om maior lado')

x = int(input('Digite o valor para o lado A: '))
y = int(input('Digite o valor para o lado B: '))
z = int(input('Digite o valor para o lado C: '))
t1 = Triangulo(x, y, z)
p = t1.calcPerimetro()
t1.getmaiorlado()
print('O perímetro do triângulo é: ', p)