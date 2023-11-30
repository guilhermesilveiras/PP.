temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range (12):
    temperatura.append(float(input('Insira a temperatura do mês de ' + meses[i] + ': ')))

media = sum(temperatura) / len(temperatura)

for i, p in enumerate(temperatura):
    if p > media:
        print(meses[i], '-> ', p)