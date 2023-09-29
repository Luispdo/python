n = int(input('Digite um número: '))
base = int(input('Escolha uma base de conversão: [1] Binário, [2] Octal e [3] Hexadecimal: '))
if base == 1:
    print('O número {} em binário é ==> {}.'.format(n, bin(n)))
elif base == 2:
    print('O número {} em octal é ==> {}.'.format(n, oct(n)))
elif base == 3:
    print('O número {} em hexadecimal é ==> {}.'.format(n, hex(n)))
else:
    print('\033[1;31mOpção inválida!\033[m')
