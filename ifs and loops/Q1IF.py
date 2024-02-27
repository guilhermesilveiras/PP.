# 1. Ler um número inteiro de dizer se é par ou
# ímpar.

x = int(input('Digite um número inteiro: '))

if x % 2 == 0:
    print(f'O número digitado {x} é um número par.')
else:
    print(f'O número digitado {x} é um numero ímpar.')