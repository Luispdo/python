dist = float(input('Qual a distância da viagem(Km)? '))
if dist <= 200:
    print('O valor da passagem será de R${:.2f}.'.format(dist * 0.5))
else:
    print('O valor da passagem será de R${:.2f}.'.format(dist * 0.45))
