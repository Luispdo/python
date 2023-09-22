vel = int(input('Digite a velocidade do veículo(Km/h): '))
if vel > 80:
    print('Você foi multado!!!')
    va = vel - 80
    print('Você estava a {}Km/h acima da velocidade permitida, sua multa será de R${:.2f}.'.format(va, (va * 7)))
else:
    print('Você não foi multado!')
