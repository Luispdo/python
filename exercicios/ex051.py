s = 0
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
dc = pt + (10 - 1) * rz # formula para calcular o décimo termo de uma progressão
for c in range(pt, dc + rz, rz):
    print('{} '.format(c), end='--> ')
print('Acabou!')
