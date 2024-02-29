# 9. Faça um programa que leia um número
# indeterminado de notas. Após esta entrada de
# dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram
# informadas.
# • Exiba todas as notas na ordem inversa à que
# foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
# • Calcule e mostre a quantidade de notas acima
# da média calculada.


notas = []
maior_nota = 0
menor_nota = float('inf')
notasTotais = 0

while True:
    nota = int(input('Digita uma nota para ser inserida: (ou um 233 para sair) '))
    if nota == 233:
        break
    else:
        notas.append(nota)
        notasTotais += nota

    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

tamanhoLista = len(notas)
print(f'Foram lidas: {tamanhoLista} notas.')
print(notas)
notas.reverse()
for nota in notas:
    print(nota)

print(f'A soma das notas foi igual a: {notasTotais}')
print(f'A média das notas foi igual a: {notasTotais/tamanhoLista}')
