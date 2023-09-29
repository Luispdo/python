print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b and b == c:
        print('Do tipo EQUILÁTERO')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('Do tipo ISÓSCELES')
    else:
        print('Do tipo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
 