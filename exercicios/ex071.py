print('=' * 45)
print('{:^45}'.format('BANCO CEV'))
print('=' * 45)
totced = 0
ced = 50
valor = int(input('Que valor você quer sacar: R$'))
total = valor
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
print('=' * 45)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')