# 6. Faça um programa que pergunte o preço de
# três produtos e informe qual produto você
# deve comprar, sabendo que a decisão é
# sempre pelo mais barato.

p1 = int(input('Informe o preço do primeiro produto: '))
p2 = int(input('Informe o preço do segundo produto: '))
p3 = int(input('Informe o preço do terceiro produto: '))

if p1 < p3 and p1 < p2:
    print(f'O produto de preço {p1} deve ser o escolhido.')
elif p2 < p1 and p2 < p3:
    print(f'O produto de preço {p2} deve ser o escolhido.')
elif p3 < p1 and p3 < p2:
    print(f'O produto de preço {p3} deve ser o escolhido.')
else:
    print('Não foi possível calcular o produto a ser escolhido.')