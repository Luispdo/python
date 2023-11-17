from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU íMPAR')
print('=-' * 15)
resultado = 0
computador = randint(0, 10)
jogador = int(input('Diga um valor (0 a 10): '))
resultado = jogador + computador
if jogador < 0 or jogador > 10:
    print('Jogada inválida! Tente novamente.')
print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado}, deu ')
