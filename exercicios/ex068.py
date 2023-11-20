from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU íMPAR')
print('=-' * 15)
ct = 0
while True:
    soma = 0
    computador = randint(0, 10)
    jogador = int(input('Diga um valor (0 a 10): '))
    soma = jogador + computador
    if jogador < 0 or jogador > 10:
        print('Jogada inválida! Tente novamente.')
        break
    jogada = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    resultado = soma % 2
    if resultado == 0:
        parimpar = 'PAR'
    else:
        parimpar = 'ÍMPAR'
    if jogada[0] == parimpar[0]:
        res = 'VENCEU!'
        ct += 1
    else:
        res = 'PERDEU!'
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, deu {parimpar}')
    print('-' * 30)
    print(f'Você {res}')
    print('=-' * 15)
    if res == 'PERDEU!':
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {ct} vezes.')
    