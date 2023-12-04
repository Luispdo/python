num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 0)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop()
print(num)
num.pop(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

val = list()
for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))
for c, v in enumerate(val):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
    