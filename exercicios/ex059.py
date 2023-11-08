menu = 0
soma = 0
mult = 0
maior = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while menu != 5:
    print('=' * 30)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    print('=' * 30)
    menu = int(input('Escolha uma opção do menu: '))
    if menu == 1:
        soma = n1 + n2
        print('O resultado da soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
    if menu == 2:
        mult = n1 * n2
        print('O resultado da multiplicação de {} por {} é igual a: {}'.format(n1, n2, mult))
    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é: {}'.format(n1, n2, maior))
    if menu == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
print('------ FIM DO PROGRAMA ------')
