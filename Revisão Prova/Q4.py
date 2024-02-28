idades = []
maior_idade = 0
menor_idade = float('inf')

for i in range(5):
    idade = int(input('Digite uma idade: '))
    idades.append(idade)

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    continue

print(f'A maior idade é igual a {maior_idade}')
print(f'A menor idade é igual a {menor_idade}')