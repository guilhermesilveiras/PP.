class Programador:

    def __init__(self, nome, funcao, salario = 0):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def aumentoSalario(self, percentualAumento):
        self.salario = self.salario*(1+percentualAumento/100)

nomeP = input('Nome do programador: ')
funcaoP = input('Função do programador: ')
salarioP = int(input('Digite o salário do programador: '))

programador1 = Programador(
# nome, funcao, salario