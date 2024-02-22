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