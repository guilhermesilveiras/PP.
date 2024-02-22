#Crie um dicionário
#d e coloque nele os
#dados fornecidos pelo usuário: nome,
#idade, telefone,endereço.
#• Também usando
#d, imprima todos os
#itens do dicionário no formato chave :
#valor, ordenado pela chave

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
telefone = input('Digite seu telefone: ')
endereco = input('Digite seu endereço: ')

d = {
    'nome': nome,
    'idade': idade,
    'telefone': telefone,
    'endereco': endereco
}

for chave, valor in d.items():
    print(f"{chave}: {valor}")