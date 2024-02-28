# 1. Ler uma lista de 5 números inteiros e
# mostre cada número juntamente com a
# sua posição na lista.

listaNumeros = [1, 2, 3, 4, 5]

for i in listaNumeros:
    print(i, ' com posição igual a : ', listaNumeros.index(i)+1)