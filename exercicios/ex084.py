pessoas = list()
dado = list()
cont = maipeso = menpeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {cont} pessoas.')
for p in pessoas:
    if p[1] > 100:
        print(f'O maior peso foi de {p[1]:.1f}Kg. Peso de {p[0]}')
    else:
        print(f'O menor peso foi de {p[1]:.1f}Kg. Peso de {p[0]}')
