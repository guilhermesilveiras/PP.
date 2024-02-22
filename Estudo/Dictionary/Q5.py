# 6. Escreva um programa que leia
# um arquivo em python (nome
# fornecido pelo usuário).
# –O programa deverá informar:
# • Quantas linhas o arquivo tem
# • A quantidade de “print” que o codigo
# possui



contador_linhas = 0
contador_print = 0

# Abre o arquivo e conta as linhas e ocorrências de "print"
with open('aleatorio.txt', 'r') as arquivo:
    for linha in arquivo:
        contador_linhas += 1
        # Conta ocorrências de "print" na linha
        contador_print += linha.count("print")

# Imprime os resultados
print(f"O arquivo possui {contador_linhas} linhas.")
print(f"A palavra 'print' aparece {contador_print} vezes no código.")