m = {}

m[(0,0)] = 1
m[(0,1)] = 4
m[(1,0)] = 3
m[(1,1)] = 0

linha = ''
for i in range(2):
    linha = ''
    for j in range(2):PISI2/q1.py
        linha = linha + str(m[(i,j)]) + ' '
    print(linha)

print(m)