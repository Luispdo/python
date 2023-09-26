from random import randint
from time import sleep
cor = {'limpa':'\033[m', 
       'verde':'\033[1;32m', 
       'amarelo':'\033[1;33m'}
num = randint(0, 5)
print('\033[1;32m-=-\033[m' * 20)
print('\033[1;33mTente acertar o número em que o computador pensou!\33[m')
print('\033[1;32m-=-\033[m' * 20)
n = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
print('O número pensado pelo computador é o {}{}{}.'.format(cor['amarelo'], num, cor['limpa']))
if num == n:
    print('PARABÉN!!! Você acertou em cheio!')
else:
    print('NÃO FOI DESSA VEZ!!! Você errou feio!')
