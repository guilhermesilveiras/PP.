pares = []
impares = []

for i in range(20):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print (pares);
print (impares)