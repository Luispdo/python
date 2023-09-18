from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('Um triangulo retângulo cujos valores dos catetos são {} e {}, terá uma hipotenusa igual a {}.'.format(co, ca, h))
