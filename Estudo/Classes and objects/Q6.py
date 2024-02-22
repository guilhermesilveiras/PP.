# Crie uma classe Aluno, que possui como atributo um nome e
# cpf. Crie outra classe chamada Equipe, que possui como
# atributo uma lista de participantes do tipo Aluno e outro
# atributo chamado projeto.
# • Crie uma terceira classe chamada GerenciadorEquipes. Essa
# classe possui como atributo uma lista de todas as equipes
# formadas. Ela deverá possuir o método criarEquipe, que
# recebe uma lista de alunos de uma equipe e diz se a equipe
# pode ser formada ou não. Caso não haja nenhum aluno da
# equipe a ser formada em uma outra equipe com o mesmo
# projeto, então a equipe é criada e acrescentada à lista. Caso
# contrário é informada que a equipe não pode ser criada.


class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, participantes, projeto):
        self.participantes = participantes
        self.projeto = projeto

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self, lista_alunos, projeto):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                print('Já existe uma equipe com o mesmo projeto.')
                return False

        nova_equipe = Equipe(lista_alunos, projeto)
        self.equipes.append(nova_equipe)
        print('Equipe criada com sucesso.')
        return True