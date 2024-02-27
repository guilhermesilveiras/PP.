# 2. Tem-se um conjunto de dados
# contendo a altura e o sexo (M ou F) de
# 15 pessoas. Faça um programa que
# calcule e mostre:
# – a maior e a menor altura do grupo
# – a média de altura das mulheres
# – o número de homens
# – o sexo da pessoa mais alta

maior_altura = float('-inf')
menor_altura = float('inf')
soma_alturas_mulheres = 0
num_homens = 0
sexo_pessoa_mais_alta = None

# Ler os dados das 15 pessoas
for i in range(15):
    altura = float(input("Digite a altura da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()

    # Verificar maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
        sexo_pessoa_mais_alta = sexo
    if altura < menor_altura:
        menor_altura = altura

    # Calcular soma das alturas das mulheres e contar o número de homens
    if sexo == 'F':
        soma_alturas_mulheres += altura
    elif sexo == 'M':
        num_homens += 1

# Calcular média de altura das mulheres
media_alturas_mulheres = soma_alturas_mulheres / 15

# Mostrar resultados
print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)
print("Média de altura das mulheres:", media_alturas_mulheres)
print("Número de homens:", num_homens)
print("Sexo da pessoa mais alta:", sexo_pessoa_mais_alta)