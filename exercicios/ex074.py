'''from random import randint
for cont in range(1, 6):
    num = int(tuple(randint(cont + 0, 10)))
    print(num)

tupla = tuple(randint(i + 1, 9) for i in range(randint(0, 5)))
print(tupla)'''

from random import sample
num = tuple(sample(range(10), 5))
#print(f'Os números gerados foram {sorted(num)}')
print(f'Os valores sorteados foram: {num}')