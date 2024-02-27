# 2. Ler a temperatura de uma pessoa e exibir a
# mensagem “Febre Alta” (temp ≥ 39), “Febril”
# (39 > temp ≥ 37) ou “Sem Febre” (temp <
# 37).

temp = int(input('Insira sua temperatura: '))

if temp >= 39:
    print(f'A temperatura inserida de {temp} é uma febre alta.')
elif temp < 39 and temp >= 37:
    print(f'A temperatura inserida de {temp} é febril.')
else:
    print('Você está sem febre.')