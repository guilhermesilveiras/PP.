# Coloque cada objeto Ponto numa lista.
# • Imprima cada elemento da lista


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

ponto_A = Ponto(100, 200)
ponto_B = Ponto(130, 150)
ponto_C = Ponto(500, 239)
Outro_Ponto = Ponto(199, 54)

lista_pontos = [ponto_A, ponto_B, ponto_C, Outro_Ponto]

for ponto in lista_pontos:
    print(ponto.x, ponto.y)