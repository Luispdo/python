print('=' * 45)
print('{: ^45}'.format('BANCO CEV'))
print('=' * 45)
valor = ced50 = ced20 = ced10 = ced1 = 0
valor = int(input('Que valor você quer sacar: R$'))
#while valor % 1 != 0:
ced50 = valor // 50
ced20 = (valor % 50) // 20
ced10 = (ced20 % 20) // 10
ced1 = (ced10 % 10) // 1
valor = ced1 % 1

print(ced50, ced20, ced10, ced1)
print('=' * 45)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')