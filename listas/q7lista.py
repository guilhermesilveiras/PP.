# 7. Faça um programa que crie uma matriz aleatoriamente.
# O tamanho da matriz deve ser informado pelo usuário.

import random

matriz = []

c = int(input('Digite um número de colunas para a matriz: '))
l = int(input('Digite um número de linhas para a matriz: '))

for i in range(l):
    novaLinha = []
    for m in range(c):
        numero = random.randint(1, 100)
        novaLinha.append(numero)
    matriz.append(novaLinha)

print(matriz)
