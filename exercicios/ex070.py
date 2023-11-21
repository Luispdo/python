print('-' * 35)
print('        LOJA SUPER BARATÃO')
print('-' * 35)
total = menorp = totmais = 0
while True:
    item = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {} produtos custando mais de R${:.2f}')
print(f'O produto mais barato foi {item} que custa R${menorp:.2f}')
