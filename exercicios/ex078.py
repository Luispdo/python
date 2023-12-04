valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
max = max(valores)
min = min(valores)
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max} na posição ', end='')
for c, v in enumerate(valores):
    if v == max:
        print(f'{c}... ', end='')
print()   
print(f'O menor valor digitado foi {min} na posição ', end='')
for c, v in enumerate(valores):
    if v == min:
        print(f'{c}... ', end='')
print()
    