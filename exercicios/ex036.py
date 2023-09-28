valor = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o salário do candidato? R$'))
prazo = int(input('Em quantos anos será pago? '))
pmês = prazo * 12
prestação = valor / pmês
print(pmês, prestação)
if sal * 0.3 >= valor / pmês:
    print('O empréstimo de R${:.2f} pelo período de {} anos, está \033[1;32mAPROVADO\033[m.'.format(valor, prazo))
    print('O valor da prestação será de R${:.2f} por mês.'.format(pmês))
else:
    print('O emprestimo foi \033[1;31mNEGADO\033[m.')
