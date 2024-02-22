# 4. Escreva um programa que leia
# um arquivo com um conjunto de
# nomes (1 por linha). O programa
# deve ordenar os nomes e gerar
# um novo arquivo com os nomes
# ordenados.



arquivo = open('nomes.txt', 'r')
listaNomes = arquivo.readlines()
arquivo.close()

listaNomes.sort()

arquivo2 = open('nomes-em-ordem.txt', 'w')
arquivo2.writelines(listaNomes)
arquivo2.close()