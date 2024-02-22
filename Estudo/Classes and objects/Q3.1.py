# 1. Crie uma classe chamada Ingresso, que
# possui um valor em reais e um método
# imprimeValor()
# – Crie uma classe VIP, que herda de Ingresso e
# possui um valor adicional. Crie um método que
# retorne o valor do ingresso VIP (com o adicional
# incluído)


class Ingresso:

    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        return self.valor

class Vip(Ingresso):

    def __init__(self, valorAdicional, valor):
        Ingresso.__init__(self, valor)
        self.valorAdicional = valorAdicional
        self.valor = self.valor + self.valorAdicional


ingresso1 = Ingresso(10)
x = ingresso1.imprimeValor()
print(x)
ingresso2 = Vip(20, 10)
y = ingresso2.imprimeValor()
print(y)

