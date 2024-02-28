# 4. Ler um vetor com 20 idades e exibir a
# maior e menor.

vetor = []
maior_idade = 0
menor_idade = float('inf')

for i in range(10):
    idade = int(input('Insira uma idade para ser inserida no vetor: '))
    vetor.append(idade)

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

print(f'A maior idade é igual a {maior_idade} e a menor idade é igual a {menor_idade}')