# 5. Inicialize uma lista de 20 números inteiros. Armazene
# os números pares em uma lista PAR e os números
# ímpares em uma lista IMPAR. Imprima as listas PAR
# e IMPAR.

pares = []
impares = []

for i in range(20):
    numero = int(input('Insira um valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)