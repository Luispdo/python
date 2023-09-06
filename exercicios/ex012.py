p = float(input('Digite o preço do produto: R$'))
d = float(input('Digite a margem de desconto: '))
np = p - p * (d / 100)
print('O novo preço do produto, com {}% de desconto é R${:.2f}.'.format(d, np))
