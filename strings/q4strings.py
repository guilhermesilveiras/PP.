# 4. Modifique o programa anterior de forma a
# mostrar o nome em formato de escada.

nome = input('Digite seu nome: ')

for i in range(len(nome)):
    print(nome[:i+1])