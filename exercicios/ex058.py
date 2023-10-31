from random import randint
from time import sleep
c = 1
cor = {'limpa':'\033[m', 
       'verde':'\033[1;32m', 
       'amarelo':'\033[1;33m'}
num = randint(0, 5)
print('\033[1;32m-=-\033[m' * 20)
print('\033[1;33mTente acertar o número em que o computador pensou!\33[m')
print('\033[1;32m-=-\033[m' * 20)
n = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(1)
while n != num:
    print('NÃO FOI DESSA VEZ!!! Você errou feio!')
    n = int(input('Tente outra vez! '))
    c += 1
print('PARABÉN!!! Você acertou em cheio!')
print('O número pensado pelo computador foi o {}{}{}. Você precisou de {}{}{} tentativas para acertar'.format(cor['amarelo'], num, cor['limpa'], cor['verde'], c, cor['limpa']))
