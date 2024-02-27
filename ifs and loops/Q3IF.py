# 3. Entrar com um distância (km) e o tempo de
# viagem (horas) de um automóvel, e dizer se
# a velocidade média foi superior ao limite
# (110 km/h) ou não.

d = int(input('Digite a distância em km da sua viagem: '))
t = int(input('Digite o tempo em horas da sua viagem: '))

if d/t > 110:
    print(f'Você fez sua viagem em uma velocidade média de {d/t}km/h e superou o limite de 110km/h')
else:
    print(f'Você fez sua viagem em uma velocidade média de {d/t}km/h e respeitou o limite de 110km/h')