from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-' * 40)
lista = []
jogos = []
tot = 1
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= njogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'========== SORTEANDO {njogos} JOGOS ==========')
for i, l in enumerate(jogos):    
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'{" < BOA SORTE! > ":=^40}')
print()
