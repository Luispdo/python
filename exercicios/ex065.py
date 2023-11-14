med = 0
maior = 0
menor = 0
soma = 0
ct = 0
fim = 'S'
while fim not in 'N':
    num = int(input('Digite um número: '))
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    ct += 1
    print(soma, ct)
    maior = num
    menor = num
    if maior > num:
        maior = num
    elif num < menor:
        menor = num
med = soma / ct
print('Foram digitados {} números e a média foi {}'.format(ct, med))


if x == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        if pesomenor > peso:
            pesomenor = peso