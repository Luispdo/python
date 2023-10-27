pesomaior = 0
pesomenor = 0
for x in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        if pesomenor > peso:
            pesomenor = peso
print('O maior peso foi {:.1f} e o menor peso foi {:.1f}.'.format(pesomaior, pesomenor))
