import random
num = random.randint(0, 5)
print('Tente acertar o número em que pensei!!!')
n = int(input('Digite um número entre 0 e 5: '))
print('O número pensado é o {}.'.format(num))
if num == n:
    print('PARABÉN!!! Você acertou em cheio!')
else:
    print('NÃO FOI DESSA VEZ!!! Você errou feio!')
