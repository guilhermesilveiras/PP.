# 5. Faça um Programa que leia três números e
# mostre-os em ordem decrescente.

x1 = int(input('Digite um valor para o primeiro número: '))
x2 = int(input('Digite um valor para o segundo número: '))
x3 = int(input('Digite um valor para o terceiro número: '))

if x1 > x2 > x3:
    print(f'{x1}, {x2}, {x3}.')
elif x1 > x3 > x2:
    print(f'{x1}, {x3}, {x2}. ')
elif x2 > x1 > x3:
    print(f'{x2}, {x1}, {x3}.')
elif x2 > x3 > x1:
    print(f'{x2}, {x3}, {x1}.')
elif x3 > x1 > x2:
    print(f'{x3}, {x1}, {x2}.')
elif x3 > x2 > x1:
    print(f'{x3}, {x2}, {x1}.')
else:
    print('Não foi possível organizar os números em ordem decrescente.')
