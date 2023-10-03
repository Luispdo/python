valor = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o salário do comprador? R$'))
prazo = int(input('Em quantos anos será pago? '))
pmês = prazo * 12
prestação = valor / pmês
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valor, prazo), end='')
print(' serão {} prestações de R${:.2f}.'.format(pmês, prestação))
if sal * 0.3 >= valor / pmês:
    print('Seu empréstimo foi \033[1;32mAPROVADO!\033[m')
else:
    print('Seu empréstimo foi \033[1;31mNEGADO!\033[m')
