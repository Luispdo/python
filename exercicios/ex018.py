import math
a = float(input('Digite um ângulo qualquer: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('Para o ângulo de valor {}°, o seno vale {:.2f}, o cosseno vale {:.2f} e a tangente vale {:.2f}.'.format(a, s, c, t))
