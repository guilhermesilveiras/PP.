from random import randint

m = {}
for i in range(3):
    for j in range(3):
        m[(i,j)] = randint(0, 10)


pares = 0
impares = 0

for i in range(3):
    for j in range(3):
        if m[(i,j)] % 2 == 0:
            pares += m[(i,j)]
        else:
            impares += m[(i,j)]
        print(m[(i, j)], end = ' ')
    print()
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')  
            

