from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU íMPAR')
print('=-' * 15)
computador = randint(0, 10)
jogada = int(input('Diga um valor (0 a 10): '))
if jogada < 0 > 10:
    print('Jogada inválida! Tente novamente.')
print(f'computador {computador} e jogador {jogada}')
