peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / altura ** 2
print('Uma pessoa que pesa {:.2f}Kg e tem {:.2f} metros de altura, tem IMC igual a {:.1f}.'.format(peso, altura, imc))
if imc < 18.5:
    print('Classificação: \033[1;33mABAIXO DO PESO\033[m')
elif imc < 25:
    print('Classificação: \033[1;32mPESO IDEAL\033[m')
elif imc < 30:
    print('Classificação: \033[1;33mSOBREPESO\033[m')
elif imc < 40:
    print('Classificação: \033[1;31mOBESIDADE\033[m')
else:
    print('Classificação: \033[1;33;41mOBESIDADE MÓRBIDA\033[m')
    