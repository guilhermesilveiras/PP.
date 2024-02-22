# Considere as classes ContaCorrente e Poupanca
# apresentadas em sala de aula. Crie uma classe
# ContaImposto que herda de conta e possui um atributo
# percentualImposto. Esta classe também possui um
# método calculaImposto() que subtrai do saldo, o valor
# do próprio saldo multiplicado pelo percentual do
# imposto. Crie um programa para criar objetos, testar
# todos os métodos e exibir atributos das 3 classes
# (ContaCorrente, Poupanca e ContaImposto).


class ContaCorrente:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

