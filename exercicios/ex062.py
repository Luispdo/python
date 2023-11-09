print('Gerador de PA')
print('-=-' * 7)
maist = 1
while maist != 0:
    pt = int(input('Digite o primeiro termo da PA: '))
    rz = int(input('Digite a razão da PA: '))
    c = 1
    t = pt
    while c <= 10:
        print('{} '.format(t), end='→ ')
        t += rz
        c += 1
    print('PAUSA')
    maist = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(c - 1))