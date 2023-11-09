print('Gerador de PA')
print('-=-' * 7)
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
c = 1
t = pt
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} '.format(t), end='→ ')
        t += rz
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
