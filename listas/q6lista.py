# 6. Faça um programa que receba a temperatura média
# de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas
# e mostre a média calculada juntamente com todas as
# temperaturas acima da média anual, e em que mês
# elas ocorreram (mostrar o mês por extenso: 1 –
# Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
temperaturaTotal = 0
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mesesAcima = []

for i in range(1, 13):
    temperatura = float(input(f'Insira a temperatura do mês {i}: '))
    temperaturas.append(temperatura)
    temperaturaTotal += temperatura
print(f'A média anual de temperatura foi igual a: {temperaturaTotal/12}')

