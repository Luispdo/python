l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = l * h
qt = a * 2
print('A quantidade de tinta para se pintar uma parede de {:.2f}m² é de {:.2f} litros.'.format(a, qt))

