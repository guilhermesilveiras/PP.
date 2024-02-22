# Faça um programa que
# escreve uma frase digitada pelo
# usuário em um arquivo. Em
# seguida o programa deve ler e
# imprimir o conteúdo desse
# arquivo

nome = input('Qual é o seu nome?')

files = open('nome.txt', 'w')
files.write(nome)
files.close()

files = open('nome.txt', 'r')
ler = files.read()
print(ler)