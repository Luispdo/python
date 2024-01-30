ficha = {}
dados = []
soma = média = 0
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if ficha['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    dados.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
média = soma / len(dados)
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] in 'F':
        print(f'|{p["nome"]}|', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in dados:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'   {k} = {v}; ', end='')
        print()
print()
print('<< ENCERRADO >>')
print()
