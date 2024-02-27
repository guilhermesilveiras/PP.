# 4. Faça um Programa que peça para entrar com
# um ano (inteiro com 4 dígitos) e determine se
# o mesmo é ou não bissexto (divisível por 4).

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')