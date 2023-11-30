string1 = input('Insira a primeira string: ')
string2 = input('Insira a segunda string: ')

print('O comprimento da primeira string é igual a', len(string1), ' e o comprimento da segunda string é igual a ', len(string2), '.')

if len(string1) == len(string2):
    print('As duas strings possuem o mesmo comprimento.')
else:
    print('As strings possuem comprimentos diferentes. ')