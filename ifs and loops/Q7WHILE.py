# 7. Faça o algoritmo de imprimir a tabuada
# de um número fornecido pelo usuário,
# usando while. Após mostrar a tabuada
# o programa deve perguntar se deseja
# imprimir a tabuada de um novo
# número.


while True:
    numero = int(input('Digite um número para calcular sua tabuada: '))
    contador = 1
    while contador <= 10:
        print(numero*contador)
        contador += 1
    continuar = input('Deseja realizar a operação com outro número? (s/n) ')
    if continuar.lower() != 's':
        break