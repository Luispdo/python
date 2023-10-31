s = 0
while s != 'M' or s != 'F':
    s = str(input('Digite o sexo: [M/F] ')).upper()
    if s == 'M' == 'F':
        print('O sexo digitado foi {}'.format(s))
    else:
        print('Opção incorreta, entre com S ou M, para encerrar!')
