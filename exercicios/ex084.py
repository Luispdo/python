pessoas = list()
dado = list()
maipeso = menpeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maipeso = menpeso = dado[1]
    else:
        if dado[1] > maipeso:
            maipeso = dado[1]
        elif dado[1] < menpeso:
            menpeso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maipeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maipeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menpeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menpeso:
        print(f'[{p[0]}] ')
print()
