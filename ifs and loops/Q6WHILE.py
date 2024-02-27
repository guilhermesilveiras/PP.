# 6. Faça um programa que peça 5 valores positivos do
# usuário (usando while). Caso o usuário digite
# algum número negativo o programa deve terminar
# imediatamente. Caso termine normalmente
# informe que os dados foram inseridos com
# sucesso (use o else).

contador = 0
numero = 5

while contador < 5:
    x = int(input('Digite um número: '))
    if x < 0:
        break
    else:
        contador += 1
        continue
print('Dados inseridos corretamente.')