# 2. Faça um programa que permita ao usuário digitar o
# seu nome e em seguida mostre o nome do usuário
# de trás para frente utilizando somente letras
# maiúsculas. Dica: lembre−se que ao informar o nome
# o usuário pode digitar letras maiúsculas ou
# minúsculas.

nome = input('Digite seu nome: ')

nome_maiusculo = nome.upper()

nome_invertido = nome_maiusculo[::-1]
print(nome_invertido)
