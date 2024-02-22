# 3. Crie um programa que implemente o
# seguinte diagrama de classe:

class Atleta:

    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        return print('Aqueceu')

class Corredor(Atleta):

    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def correr(self):
        return print('Correr')

class Nadador(Atleta):

    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def nadar(self):
        return print('Nadar')

class Ciclista(Atleta):

    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def pedalar(self):
        return print('Pedalou')

class TriAtleta(Corredor, Nadador, Ciclista):

    def __init__(self, aposentado, peso):
        Corredor.__init__(self, aposentado, peso)
        Nadador.__init__(self, aposentado, peso)
        Ciclista.__init__(self, aposentado, peso)

t1 = TriAtleta(False, 10)
print(isinstance(t1, Atleta))

t1.correr()
t1.nadar()
t1.pedalar()


