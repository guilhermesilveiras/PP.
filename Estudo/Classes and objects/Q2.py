# Classe Funcionário: Implemente a classe
# Funcionário. Um funcionário tem um nome e um
# salário. Escreva um construtor com dois parâmetros
# (nome e salário) e o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do
# funcionário em uma certa porcentagem. Exemplo
# de uso:
# harry=funcionário("Harry",25000)
# harry.aumentarSalario(10)
#
# Faca um programa que teste o método da classe.

class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentualAumento):
        self.salario = self.salario*(1+porcentualAumento/100)

funcionario1 = Funcionario("Harry", 1000)
funcionario1.aumentarSalario(10)

print(funcionario1.nome, " — ", funcionario1.salario)
