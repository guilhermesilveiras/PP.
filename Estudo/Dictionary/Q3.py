# 3. Crie um programa que cadastre
# informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as
# pessoas menores de 18 anos do
# dicionário e coloque em outro dicionário.

pessoas = {}

while True:
    nome = input("Digite o nome da pessoa (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")
    pessoas[nome] = {'idade': idade, 'cpf': cpf}

menores_de_18 = {}

for nome, info in pessoas.items():
    if info['idade'] < 18:
        menores_de_18[nome] = info

for nome in menores_de_18:
    del pessoas[nome]

print("Pessoas maiores de 18 anos:", pessoas)
print("Pessoas menores de 18 anos:", menores_de_18)