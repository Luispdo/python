from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('\033[1;33m=\033[m' * 25)
print('\033[1;32m=       JO-KEN-PÔ       =\033[m')
print('\033[1;33m=\033[m' * 25)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PÔ!!!'), sleep(1)
print('\033[1;36m-=\033[m' * 12)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[1;36m-=\033[m' * 12)
