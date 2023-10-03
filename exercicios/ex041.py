from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('Este atleta tem {} anos, sua categoria é: \033[1;34mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('Este atleta tem {} anos, sua categoria é: \033[1;34mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('Este atleta tem {} anos, sua categoria é: \033[1;34mJUNIOR\033[m'.format(idade))
elif idade <= 25:
    print('Este atleta tem {} anos, sua categoria é: \033[1;34mSÊNIOR\033[m'.format(idade))
else:
    print('Este aluno tem {} anos, sua categoria é: \033[1;34mMASTER\033[m'.format(idade))
    