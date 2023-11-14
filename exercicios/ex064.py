num = 0
soma = 0
ct = 0
print('Entre com alguns valores para obter sua soma. Para encerrar, digite 999.')
num = int(input('Digite um valor: '))
while num != 999:
    soma += num
    ct += 1
    num = int(input('Digite um valor: '))
print('Foram digitados {} números e a soma entre eles é igual a {}.'.format(ct, soma))
