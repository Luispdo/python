sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    aum = sal + (sal * 0.10)
if sal <= 1250:
    aum = sal + (sal * 0.15)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aum))
