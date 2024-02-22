class Carro:

    def __init__(self, consumo, combustivel = 0):
        self.consumo = consumo
        self.combustivel = combustivel

    def andar(self, distancia):
        if distancia > self.combustivel*self.consumo:
            print('Não há gasolina suficiente para essa viagem!')
        else:
            self.combustivel = self.combustivel - distancia/self.consumo

    def abastecer(self, gasolina):
        self.combustivel = self.combustivel + gasolina

    def obterGasolina(self):
        return self.combustivel

meuGol = Carro(30)
meuGol.abastecer(1)
meuGol.andar(30)
restante = meuGol.obterGasolina()
print(restante)


