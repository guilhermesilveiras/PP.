nomes = []

with open('nomes.txt') as file:
    for line in file:
        nomes.append(line.rstrip())

for nome in sorted(nomes):
    print(f'Olá, {nome}')





