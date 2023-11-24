lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[:3])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)