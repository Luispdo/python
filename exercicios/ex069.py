total18 = homens = mulheres20 = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('')
print('====== FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todos temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
print('')
