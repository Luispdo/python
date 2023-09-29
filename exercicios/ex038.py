n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro valor "{}" é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor "{}" é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais')
    