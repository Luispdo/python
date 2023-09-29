from datetime import date
ano = int(input('Entre com o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade < 17:
    print('Você tem agora {} anos, ainda faltam {} anos para vc se alistar.'.format(idade, 17 - idade))
elif idade >= 17 and idade <= 18:
    print('Você tem agora {} anos e portanto, está no período de se alistar.'.format(idade))
else:
    print('Você tem agora {} anos, já passou {} anos do prazo de alistamento.'.format(idade, idade - 18))
