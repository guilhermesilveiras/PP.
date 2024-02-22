# Escreva um programa que lê um arquivo
# contendo a identidade e o nome de várias
# pessoas, no seguinte formato
#
# 5384423 Manoel
# 4345566 Alberto
# 3235574 Mariana
#
# ...
# o programa deve gerar um dicionário onde as
# chaves são as identidades e os valores os
# nomes. Ao final o programa deve exibir o
# dicionário.


arquivo = open('aleatorio.txt')
dicionario = {}
for linha in arquivo:
    cpf, nome = linha.split()
    dicionario[int(cpf)] = nome

arquivo.close()

print('Dicionário de pessoas: ')
print(dicionario)

