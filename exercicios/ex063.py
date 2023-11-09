print('-' * 27)
print('  Sequência de Fibonacci')
print('-' * 27)
nf = int(input('Digite quantos termos da Sequência de Fibonacci você quer ver: '))
t1 = 0
t2 = 1
print('~' * nf * 5)
print('{} → {} '.format(t1, t2), end='→ ')
c = 3
while c <= nf:
    t3 = t1 + t2
    print('{} '.format(t3), end='→ ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
print('~' * nf * 5)
