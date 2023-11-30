dna = input('Digite uma sequência de DNA: ')

# Tabela de transformação de DNA para RNA
dna_para_rna = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

rna = ''.join([dna_para_rna[base] for base in dna])

print('A sequência de RNA correspondente é: ' + rna)