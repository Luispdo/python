ct = s = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    ct += 1
    s += num
print(f'Foram digitados {ct} números que somados valem {s}!')
