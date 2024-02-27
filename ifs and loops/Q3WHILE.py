# 3. Faça um programa que imprima o
# fatorial de um número. O valor de
# entrada deve ser menor ou igual a 20.

numero = int(input("Digite um número (0 a 20): "))

if numero < 0 or numero > 20:
    print("O valor de entrada deve ser um número entre 0 e 20.")
else:
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado *= contador
        contador += 1
    print("O fatorial de", numero, "é", resultado)