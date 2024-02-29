# 3. Crie um programa que cadastre
# informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as
# pessoas menores de 18 anos do
# dicionário e coloque em outro dicionário.

pessoas = {}

while True:
    nome = input('Digite seu nome: (ou sair para sair) ')
    if nome.lower() == 'sair':
        break
    idade = int(input('Digite sua idade: '))
    cpf = input('Digite seu cpf: ')
    pessoas[nome] = {'idade': idade, 'cpf': cpf}

menos_de_18 = {}

for nome, i in pessoas.items():
    if i['idade'] <= 18:
        menos_de_18[nome] = i

for nome in menos_de_18:
    del pessoas[nome]

print('Pessoas maiores de 18: ', pessoas)
print('Pessoas menores de 18: ', menos_de_18)