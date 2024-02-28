nome = 'Isabel Cristina Leopoldina'
nome += ' Augusta Micaela Gabriela'
nome += ' Rafaela Gonzaga de Orleans'
nome += ' e Brangaça'

l = nome.split('Leopoldina ')
y = ''.join(l)
l = y.split('Gonzaga ')
nomeDef = ''.join(l)
print(nomeDef)