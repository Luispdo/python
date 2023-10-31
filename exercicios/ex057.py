s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção incorreta. Por favor, informe o seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))
        