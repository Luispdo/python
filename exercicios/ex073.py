times = ('Palmeiras', 'Flamengo', 'Botafogo', 'Atlético-MG',
         'Gremio', 'Bragantino', 'Fluminense', 'Atlético-PR',
         'Cuiabá', 'São Paulo', 'Internacional', 'Fortaleza',
         'Corinthians', 'Santos', 'Vasco da Gama', 'Bahia',
         'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Cruzeiro está na {times.index("Cruzeiro") + 1}ª posição')
print('')
