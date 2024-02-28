# 3. Ler uma lista com 4 notas, em seguida
# o programa deve exibir as notas e a
# média.

listaNotas = []
totalNotas = 0

for i in range(4):
    notas = (int(input(f'Digite a {i+1}° nota: ')))
    listaNotas.append(notas)
    totalNotas += notas

print(listaNotas)
print(f'Sua média foi igual a: {totalNotas/4}')