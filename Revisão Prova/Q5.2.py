def fatorialFor(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

y = fatorialFor(5)
print(y)