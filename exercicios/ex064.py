num = 0
soma = 0
ct = 0
print('Entre com alguns valores para obter sua soma. Para encerrar, digite 999.')
if num != 999:
    while num != 999:
        num = int(input('Digite um valor: '))
        soma += num
        ct += 1
print('Foram digitados {} números e a soma entre eles é igual a {}.'.format(ct - 1, soma))
