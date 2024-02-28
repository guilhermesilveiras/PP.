# 1. Uma fábrica tem 10 representantes. Cada um
# recebe uma comissão calculada a partir do
# número de itens de um pedido, segundo os
# seguintes critérios:
# – para até 19 itens vendidos, a comissão é de 10%
# do valor total do pedido;
# – para pedidos de 20 e 49 itens, a comissão é de
# 15% do valor total do pedido;
# – para pedidos de 50 a 74 itens, a comissão é de
# 20% do valor total do pedido; e
# – para pedidos iguais ou superiores, a 75 itens a
# comissão é de 25%.
# Faça um programa que lê a quantidade de
# itens de pedidos de cada representante e
# imprime o percentual de comissão de cada
# um.


for i in range(5):
    nPedidos = int(input('Quantos pedidos você vendeu? '))
    valor = int(input('E qual foi o valor total da venda? '))
    if nPedidos <= 19:
        print(f'O valor de sua comissão é igual a', 0.10*valor)
    elif 20 <= nPedidos <= 49:
        print('O valor de sua comissão é igual a ', 0.15*valor)
    elif 50 <= nPedidos <= 74:
        print('O valor de sua comissão é igual a ', 0.20*valor)
    elif nPedidos >= 75:
        print('O valor de sua comissão é igual ', 0.25*valor)
    continue
