n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O número MAIOR é igual a {} e o MENOR é igual a {}.'.format(maior, menor))
