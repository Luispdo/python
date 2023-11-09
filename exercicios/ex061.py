print('Gerador de PA')
print('-=-' * 7)
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
c = 1
t = pt
while c <= 10:
    print('{} '.format(t), end='→ ')
    t += rz
    c += 1
print('Acabou!')
