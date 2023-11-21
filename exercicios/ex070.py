print('-' * 35)
print('{: ^35}'.format('LOJA SUPER BARATÃO'))
print('-' * 35)
totp = menorp = totmil = ct = 0
while True:
    item = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    totp += preço
    ct += 1
    resp = ' '
    if preço >= 1000:
        totmil += 1
    if ct == 1:
        menorp = preço
        itemb = ' '
    else:
        if preço < menorp:
            menorp = preço
            itemb = item
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('')
print(f'O total da compra foi R${totp:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {itemb} que custa R${menorp:.2f}')
print('')