def fatorialWhile(n):
    fatorial = 1
    contador = 1

    while contador <= n:
        fatorial *= contador
        contador += 1
    return fatorial


x = fatorialWhile(5)
print(x)