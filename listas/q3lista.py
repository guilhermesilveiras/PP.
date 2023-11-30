notas = []

for i in range (4):
    notas.append(float(input('Insira uma nota: ')))

print('Notas: ', notas)
print('Média: ', sum(notas)/len(notas))