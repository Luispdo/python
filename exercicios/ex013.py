s = float(input('Digite o salário do funcionário: '))
i = float(input('Digite o índice da aumento: '))
a = s + s * (i / 100)
print('O salário do funcionário, com {:.2f}% de aumento, será de R${:.2f}.'.format(i, a))
