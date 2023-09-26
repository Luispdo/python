n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('A soma de\033[32m {}\033[m e\033[34m {}\033[m é igual a \033[1;4;31;43m{}\033[m'.format(n1,n2,s))
