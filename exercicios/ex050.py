s = 0
for x in range(1, 7):
    num = int(input('Digite o {}º número: '.format(x)))
    if num % 2 == 0:
        s += num
print('A soma dos números pares dessa sequência é: {}'.format(s))
