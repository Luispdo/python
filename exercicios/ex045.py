from time import sleep
from random import randint
comp = randint(0, 2)
print('\033[1;33m=\033[m' * 25)
print('\033[1;32m=       JO-KEN-PÔ       =\033[m')
print('\033[1;33m=\033[m' * 25)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? ')), sleep(1)
print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PÔ!!!')
print('-=' * 12)
'''print('Computador jogou {}'.format())'''
