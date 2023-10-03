print('\033[1;32m-=\033[m' * 12)
print('\033[1;33mAnalisador de Triângulos\033[m')
print('\033[1;32m-=\033[m' * 12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
 