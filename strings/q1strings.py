# 1. Faça um programa que leia 2 strings e
# informe o conteúdo delas seguido do
# seu comprimento. Informe também se
# as duas strings possuem o mesmo
# comprimento e são iguais ou diferentes
# no conteúdo.

string1 = input('Digite uma palavra: ')
string2 = input('Digite outra palavra: ')

print('A primeira palavra que você escreveu foi: ', string1, ', e a segunda palavra foi: ', string2)

if len(string1) == len(string2):
    print('As palavras digitadas tem o mesmo comprimento!')
else:
    print('As palavras digitadas tem comprimento diferente.')

if string1 == string2:
    print('As palavras digitadas são iguais!')
else:
    print('As palavras digitadas são diferentes.')