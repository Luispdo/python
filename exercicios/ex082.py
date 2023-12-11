lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
print()
