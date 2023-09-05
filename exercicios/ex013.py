s = float(input('Digite o salário do funcionário: '))
i = float(input('Digite o índice da aumento: '))
a = s + s * (i / 100)
print('O funcionário que recebe R${} de salário, terá um aumento de {:.2f}% e passará a receber um salário de R${:.2f}.'.format(s, i, a))
