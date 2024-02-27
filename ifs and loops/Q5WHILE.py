# 5. Faça um algoritmo que peça dois números – base
# e expoente – calcule e mostre o primeiro número
# elevado ao segundo número. Não utilize a função
# de potência da linguagem.

base = int(input('Digite um número que servirá como base: '))
expoente = int(input('Digite um número que servirá como expoente: '))

contador = 1

while contador < expoente:
    base *= base
    contador +=1
print(f'O número base elevado ao expoente é igual a {base}')