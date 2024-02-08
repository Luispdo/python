#print(x)
'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'   \033[0;31mProblema encontrado foi {erro.__class__}\033[m')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')'''
    
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[0;31m   -> Tivemos um problema com os tipos de dados que foram digitados\033[m')
except ZeroDivisionError:
    print('\033[0;31m   -> Não é possível dividir um número por zero!\033[m')
except KeyboardInterrupt:
    print('\033[0;31m   -> O usuário preferiu não informar os dados!\033[m')
except Exception as erro:
    print(f'   \033[0;31mProblema encontrado foi {erro.__cause__}\033[m')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
