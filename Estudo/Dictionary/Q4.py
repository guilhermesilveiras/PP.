# 4. Considere um sistema onde os dados são
# armazenados em dicionários. Nesse sistema
# existe um dicionario principal e o dicionário
# de backup. Cada vez que o dicionário
# principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie
# um programa que insira dados em um
# dicionário, realizando o backup a cada dado
# e excluindo os dados do dicionário principal
# quando ele atingir tamanho 5.


dicionario_principal = {}
dicionario_backup = {}

# Loop para inserir dados no dicionário principal
while True:
    chave = input("Digite a chave (ou 'sair' para encerrar): ")
    if chave == 'sair':
        break
    valor = input("Digite o valor: ")

    # Inserir dados no dicionário principal e fazer backup
    dicionario_principal[chave] = valor
    dicionario_backup[chave] = valor

    # Se o dicionário principal atingir tamanho 5, imprimir e limpar
    if len(dicionario_principal) == 5:
        print("Dicionário principal:")
        for chave, valor in dicionario_principal.items():
            print(f"{chave}: {valor}")
        dicionario_principal.clear()

# Verificar se há dados restantes no dicionário principal para imprimir
if dicionario_principal:
    print("Dicionário principal:")
    for chave, valor in dicionario_principal.items():
        print(f"{chave}: {valor}")

# Imprimir o dicionário de backup
print("Dicionário de backup:")
for chave, valor in dicionario_backup.items():
    print(f"{chave}: {valor}")