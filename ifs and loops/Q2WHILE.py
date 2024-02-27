# 2. Escreva um programa que lê uma quantidade
# indeterminada de números inteiros e escreve
# todos os que forem ímpares positivos (use o
# ‘continue’. Considerar o valor 99 como fim da
# entrada.

x = 99

while x > 0:
    x = x-1
    if x%2 == 0:
        continue
    print(x)
else:
    print('Fim do teste.')