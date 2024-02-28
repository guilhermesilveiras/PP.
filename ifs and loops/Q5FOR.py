# 5. O Departamento Estadual de
# Meteorologia te contratou para
# desenvolver um programa que leia um
# conjunto de 100 temperaturas, e informe
# ao final a menor e a maior temperaturas
# informadas, bem como a média das
# temperaturas.

temperaturas = 0
maior_temp = 0
menor_temp = float('inf')

for i in range(5):
    temperatura = float(input('Digite uma temperatura para comparação: '))
    temperaturas += temperatura

    if temperatura > maior_temp:
        maior_temp = temperatura
    if temperatura < menor_temp:
        menor_temp = temperatura
    continue

print(f'A maior temperatura registrada: {maior_temp}, a menor temperatura: {menor_temp} e a média é: ', temperaturas/5 )