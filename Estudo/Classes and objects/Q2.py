class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentualAumento):
        self.salario = self.salario*(1+porcentualAumento/100)

funcionario1 = Funcionario("Harry", 1000)
funcionario1.aumentarSalario(10)

print(funcionario1.nome, " — ", funcionario1.salario)
