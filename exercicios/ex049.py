n = int(input('Digite um número para ver sua tabuada: '))
m = 0
print('-' * 12)
for m in range(0, 11):
    print('{} x {:2} = {}'.format(n, m, n*m))
    m == m + 1
print('-' * 12)
    