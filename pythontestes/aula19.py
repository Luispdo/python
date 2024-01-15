'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
pessoas ['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas)'''

brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado3 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

print(brasil)
print(brasil[1])
print(brasil[0]['uf'])