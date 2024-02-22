# Construa uma classe Produto, que deve ter
# os atributos codigo e preco (privados).
# Adicione também um atributo estático
# qtdProd, que deverá ser acrescentado toda
# vez que um novo objeto é criado.
# – Crie os métodos get e set e teste a classe.


class Produto:

    qtdProd = 0

    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.qtdProd += 1

    def mostrarQtd(self):
        print('Total de produtos: %d'%Produto.qtdProd)

    def getPreco(self):
        return self.__preco

    def setPreco(self, valor):
        self.__preco = valor
        return self.__preco

p1 = Produto(232, 22.90)
p1.setPreco(10.90)
x = p1.getPreco()
print(x)
p2 = Produto(233, 10.50)
p3 = Produto(234, 10.60)
y = p3.mostrarQtd()
print(y)