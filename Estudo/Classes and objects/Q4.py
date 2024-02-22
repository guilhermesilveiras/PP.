# 4. Implemente uma classe Aluno, que deve ter os
# seguintes atributos: nome, curso, tempoSemDormir
# (em horas). Essa classe deverá ter os seguintes
# métodos:
# – estudar (que recebe como parâmetro a qtd de horas de
# estudo e acrescenta tempoSemDormir )
# – Dormir (que recebe como parâmetro a qtd de horas de
# sono e reduz tempoSemDormir )
#
# • Crie um código de teste da classe, criando um objeto
# da classe aluno e usando os métodos estudar e
# dormir. Ao final imprima quanto tempo o aluno está
# sem dormir


class Aluno:

    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, estudo):
        self.tempoSemDormir = self.tempoSemDormir + estudo
        return self.tempoSemDormir

    def sono(self, dormir):
        self.tempoSemDormir = self.tempoSemDormir - dormir
        return self.tempoSemDormir


nome = input('Digite seu nome: ')
curso = input('Digite seu curso: ')
semdormir = int(input('Há quantas horas você está sem dormir?'))
al1 = Aluno(nome, curso, semdormir)
print('Seu nome é ', al1.nome, ', seu curso é: ', al1.curso, ', e você está sem dormir há ', al1.tempoSemDormir, ' horas')
al1.estudar(10)
print('Depois de estudar, você está sem dormir há ', al1.tempoSemDormir, ' horas')
al1.sono(5)
print('Depois de dormir você está ')