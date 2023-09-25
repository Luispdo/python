dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(dist))
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
