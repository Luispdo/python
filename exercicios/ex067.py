m = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 12)
    for m in range(0, 11):
        print(f'{n} x {m:2} = {n * m}')
        m == m + 1
    print('-' * 12)
print('Acabou!')
