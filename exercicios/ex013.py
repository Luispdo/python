s = float(input('Digite o salário do funcionário: R$'))
i = float(input('Digite o índice de aumento: '))
a = s + s * (i / 100)
print('O funcionário que recebe R${:.2f} de salário, com um aumento de {:.2f}%, passará a receber um salário de R${:.2f}.'.format(s, i, a))
