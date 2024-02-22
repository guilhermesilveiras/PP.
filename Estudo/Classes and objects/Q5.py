# Classe carro: Implemente uma classe chamada Carro com as
#
# seguintes propriedades:
#
# • Um veículo tem um certo consumo de combustível (medidos em km /
#
# litro) e uma certa quantidade de combustível no tanque.
#
# • O consumo é especificado no construtor e o nível de combustível
#
# inicial é 0.
#
# • Forneça um método andar( ) que simule o ato de dirigir o veículo por
# uma certa distância, reduzindo o nível de combustível no tanque de
# gasolina. Esse método recebe como parâmetro a distância em km.
# • Forneça um método obterGasolina( ), que retorna o nível atual de
#
# combustível.
#
# • Forneça um método adicionarGasolina( ), para abastecer o tanque.
# • Faça um programa para testar a classe Carro. Exemplo de uso:
# meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de
# combustível.
# meuFusca.andar(100); # anda 100 quilômetros.
# meuFusca.obterGasolina() # Imprime o combustível que resta no
# tanque.


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


