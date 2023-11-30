lista = []

for i in range (5):
    lista.append(int(input('Insira um número: ')))

for i, p in enumerate(lista):
    print( i + 1, '-> ', p)