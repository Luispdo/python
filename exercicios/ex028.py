from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Tente acertar o número em que o computador pensou!')
print('-=-' * 20)
n = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
print('O número pensado pelo computador é o {}.'.format(num))
if num == n:
    print('PARABÉN!!! Você acertou em cheio!')
else:
    print('NÃO FOI DESSA VEZ!!! Você errou feio!')
