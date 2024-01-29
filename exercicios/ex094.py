ficha = []
dados = []
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'SN':
        print('ERRO! Por favor, digite apenas M ou F.')
    idade = int(input('Idade: '))
    #media = (nota1 + nota2) / 2
    ficha.append([nome, sexo, idade, media])
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break