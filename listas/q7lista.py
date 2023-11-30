import random

n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        num = random.randint(1, 100)  # gera um número aleatório entre 1 e 100
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print(linha)