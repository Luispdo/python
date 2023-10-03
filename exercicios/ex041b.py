from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: \033[1;34mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[1;34mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[1;34mJUNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[1;34mSÊNIOR\033[m')
else:
    print('Categoria: \033[1;34mMASTER\033[m')
 