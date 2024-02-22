# 3. Crie um programa que cadastre
# informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as
# pessoas menores de 18 anos do
# dicionário e coloque em outro dicionário.

def cadastrar_pessoa():
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    cpf = input('Digite o CPF da pessoa: ')
    return {'nome': nome, 'idade': idade, 'cpf': cpf}

def main():
    pessoas = []
    menores_de_18 = []

    continuar = True
    while continuar:
        pessoa = cadastrar_pessoa()
        pessoas.append(pessoa)
        continuar = input('Deseja cadastrar outra pessoa? (s/n): ').lower() == 's'

    # Separando pessoas menores de 18 anos
    for pessoa in pessoas:
        if pessoa['idade'] < 18:
            menores_de_18.append(pessoa)

    # Removendo pessoas menores de 18 anos da lista principal
    for pessoa in menores_de_18:
        pessoas.remove(pessoa)

    print("\nLista de todas as pessoas cadastradas:")
    for pessoa in pessoas:
        print(pessoa)

    print("\nLista de pessoas menores de 18 anos:")
    for pessoa in menores_de_18:
        print(pessoa)

if __name__ == "__main__":
    main()