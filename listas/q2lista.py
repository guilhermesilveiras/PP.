# 2. Ler uma lista de 10 números reais e
# mostre-os na ordem inversa.

listaNumeros = []

for i in range(10):
    listaNumeros.append(int(input('Digite um valor para entrar na lista: ')))
    listaNumeros.reverse()

print(listaNumeros)