s = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s = s + c
        #print(s)
print('A soma dos números impares entre 1 e 500 é igual a: {}'.format(s))
