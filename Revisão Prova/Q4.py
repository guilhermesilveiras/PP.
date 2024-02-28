idades = []

for i in range(5):
    idade = int(input('Digite a sua idade: '))
    idades.append(idade)

maior_idade = idades[0]
menor_idade = idades[0]

for idade in idades:
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

print(f'Maior idade: {maior_idade}, menor idade: {menor_idade}')