palavra = 'palavra_secreta'  # substitua por sua palavra
letras_adivinhadas = []
erros = 0

while erros < 6 and not set(palavra).issubset(set(letras_adivinhadas)):
    print(''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra]))
    palpite = input('Adivinhe uma letra: ')
    if palpite in letras_adivinhadas:
        print('Você já adivinhou essa letra.')
        continue
    if palpite in palavra:
        letras_adivinhadas.append(palpite)
    else:
        erros += 1

if set(palavra).issubset(set(letras_adivinhadas)):
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu. A palavra era ' + palavra)