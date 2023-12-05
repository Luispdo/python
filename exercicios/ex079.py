valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '    
    while resp not in 'SN':
        resp = str(input('Quer continuar? [SN] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
