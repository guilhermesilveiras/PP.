# 8. Faça um programa que crie uma matriz M (com valores
# informados do usuário) e mostre a matriz com o dobro
# dos valores lidos (2*M).

m = []

qtdeLinhas = int(input('Digita uma quantidade de linhas: '))
qtdeColunas = int(input('Digite uma quantidade de colunas: '))

for i in range(qtdeLinhas):
    novaLinha = []
    for c in range(qtdeColunas):
        numero = int(input('Digite um valor desejado para o número: '))
        numero *= 2
        novaLinha.append(numero)
    m.append(novaLinha)

print(m)