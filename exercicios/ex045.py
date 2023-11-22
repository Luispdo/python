from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
while True:
    print('\033[1;33m=\033[m' * 25)
    print('\033[1;32m=       JO-KEN-PÔ       =\033[m')
    print('\033[1;33m=\033[m' * 25)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jog = ' '
    while jog != 0 and jog != 1 and jog != 2:
        jog = int(input('Qual é a sua jogada? '))
    print('{:-<34}'.format('\033[1;31mJO \033[m')), sleep(1)
    print('{:-^34}'.format('\033[1;31m KEN \033[m')), sleep(1)
    print('{:->34}'.format('\033[1;31m PÔ\033[m')), sleep(1)
    print('\033[1;36m-=\033[m' * 12)
    print('Computador jogou {}'.format(itens[comp]))
    print('Jogador jogou {}'.format(itens[jog]))
    print('\033[1;36m-=\033[m' * 12)
    if comp == 0:
        if jog == 0:
            print('\033[1;33mJOGO EMPATADO!\033[m')
        elif jog == 1:
            print('\033[1;32mJOGADOR VENCEU!\033[m')
        elif jog == 2:
            print('\033[1;34mCOMPUTADOR VENCEU!\033[m')
    elif comp == 1:
        if jog == 0:
            print('\033[1;34mCOMPUTADOR VENCEU!\033[m')
        elif jog == 1:
            print('\033[1;33mJOGO EMPATADO!\033[m')
        elif jog == 2:
            print('\033[1;32mJOGADOR VENCEU!\033[m')
    elif comp == 2:
        if jog == 0:
            print('\033[1;32mJOGADOR VENCEU!\033[m')
        elif jog == 1:
            print('\033[1;34mCOMPUTADOR VENCEU!\033[m')
        elif jog == 2:
            print('\033[1;33mJOGO EMPATADO!\033[m')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Mais uma vez? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('')
print('Jogo encerrado! Volte sempre.')
print('')
