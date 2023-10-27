from datetime import date
anoatual = date.today().year
smaior = 0
smenor = 0
for c in range(1, 8):
    data = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if anoatual - data < 21:
        smaior += 1
    else:
        smenor += 1
print('{} pessoas já atingiram a maioridade (21 anos).'.format(smaior))
print('{} pessoas ainda não atingiram a maioridade (21 anos).'.format(smenor))
      