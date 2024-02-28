# 3. Em uma eleição presidencial com 15 eleitores
# existem 3 candidatos. Os votos são informados por
# meio de código. Os códigos utilizados são:
# – 1 – Candidato A, 2 -Candidato B, 3 – Candidato C, 4 -
# Voto Nulo e 5 - Voto em Branco
#
# Faça um programa que leia os votos de cada eleitor,
# calcule e mostre:
# – O total de votos para cada candidato
# – O total de votos nulos
# – O total de votos em branco
# – A percentagem de votos nulos sobre o total de votos;
# – A percentagem de votos em branco sobre o total de
# votos.

votosA = 0
votosB = 0
nulos = 0
brancos = 0

for i in range(15):
    voto = int(input('Insira o número de seu voto (1, 2, 3, 4): '))
    if voto == 1:
        votosA += 1
    elif voto == 2:
        votosB += 1
    elif voto == 3:
        nulos += 1
    elif voto == 4:
        brancos += 1
    continue

print(f'O total de votos por candidato foram: Candidato A: {votosA}, Candidato B: {votosB}, Nulos: {nulos}, Brancos: {brancos}')
print(f'A porcentagem de votos nulos foi igual a: ', (100*nulos)/15, '%')
print(f'A porcentagem de votos brancos foi igual a: ', (100*brancos)/15, '%')