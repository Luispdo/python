n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))
    