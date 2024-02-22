# 5. Faça um programa que leia as
# linhas de 3 a 5 de um arquivo de
# texto (considere que tem mais
# do que 5 linhas).
# –Copie as linhas selecionadas em
# um novo arquivo.

f = open("nomes.txt", "r")
linha = f.readline()
linha = f.readline()
resultado = f.readline()
resultado += f.readline()
resultado += f.readline()
f.close()
arqSaida = open("linhas3a5.txt", "w")
arqSaida.write(resultado)
arqSaida.close()
print("Gravei estas linhas no arquivo:", resultado)