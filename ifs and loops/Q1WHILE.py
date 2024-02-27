# 1. Crie um programa que lê as idades e alturas
# de alguns alunos. A condição de parada é a
# altura = 0. Em seguida, o programa deve
# informar quantos alunos com mais de 13
# anos possuem altura inferior à 1.5.

alunos_na_lista = 0

while True:
    idade = int(input('Digite um valor para a idade do aluno (ou 0 para sair): '))
    if idade == 0:
        break
    altura = float(input('Digite um valor para a altura do aluno: '))

    if idade > 13 and altura < 1.5:
        alunos_na_lista +=1

print(f'O número de alunos maiores que 13 anos e menores que 1.5 é igual a {alunos_na_lista}')

