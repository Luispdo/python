ficha = {}
dados = []
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if ficha['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))
    dados.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(dados)
