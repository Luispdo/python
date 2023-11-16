med = soma = ct = maior = menor = 0
fim = 'S'
while fim not in 'N':
    num = int(input('Digite um número: '))
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    ct += 1
    if ct == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
           menor = num
med = soma / ct
print('Foram digitados {} números e a média foi {:.2f}'.format(ct, med))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
