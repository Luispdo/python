nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome {}, tem {} letras'.format(lista[0], len(lista[0])))
