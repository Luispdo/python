from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-' * 40)
jogo = []
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'========== SORTEANDO {njogos} JOGOS ==========')
for j in range(1, njogos + 1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
            if cont >= 6:
                break
    jogo.sort()
    print(f'Jogo {j}: {jogo}')
    jogo.clear()
    njogos += 1
    sleep(1)
print(f'{" < BOA SORTE! > ":=^40}')
print()
