# 4. Faça um programa que identifica os 15
# primeiros números primos (utilizando a
# instrução break).

contador = 0
numero = 2

while contador < 15:
    eh_primo = True
    divisor = 2
    while divisor <= numero ** 0.5:  # Verifica apenas até a raiz quadrada do número
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    if eh_primo:
        print(numero, end=" ")
        contador += 1
    numero += 1
