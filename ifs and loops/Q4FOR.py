# 4. Faça um programa que peça 10 números
# inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números
# impares.

numeros_pares = 0
numeros_impares = 0

for i in range(10):
    numero = int(input('Digite o número: '))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares +=1
    continue

print(f'A quantidade de números pares inseridos foi: {numeros_pares}, e a quantidade de números impares foi: {numeros_impares}')