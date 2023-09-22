ano = int(input('Entre com um ano qualquer(aaaa): '))
if ano % 4 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bisssexto.'.format(ano))
    