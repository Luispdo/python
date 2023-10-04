print(('=' * 10), end='')
print((' LOJAS GUANABARA '), end='')
print('=' * 10)
preço = float(input('Qual o preço do produto? R$'))
print('''Condições de pagamento:
      [ 1 ] À vista no dinheiro/PIX
      [ 2 ] À vista no cartão
      [ 3 ] Até 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
cpag = int(input('Escolha uma condição de pagamento: '))
if cpag == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, (preço - preço * 0.1)))
elif cpag == 2:
    
    