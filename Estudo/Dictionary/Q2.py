# Crie um dicionário que é uma agenda e
# coloque nele os seguintes dados: chave (cpf),
# nome, idade, telefone. O programa deve ler
# um número indeterminado de dados, criar a
# agenda e imprimir todos os itens do
#
# dicionário no formato chave: nome-idade-
# fone.

def main():
    agenda = {}
    while True:
        cpf = input('Digite o CPF (ou deixe em branco para sair): ')
        if not cpf:
            break

        nome = input('Digite o nome: ')
        idade = input('Digite a idade: ')
        telefone = input('Digite o telefone: ')

        agenda[cpf] = {
            'nome': nome,
            'idade': idade,
            'telefone': telefone
        }

    for cpf, dados in agenda.items():
        print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")

if __name__ == "__main__":
    main()