d = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados? '))
vd = d * 60
vkm = km * 0.15
print('O total a pagar é de R${:.2f}'.format(vd + vkm))
