x = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(x))
print('O que foi digitado só tem espaços? ', x.isspace())
print('O que foi digitado é alfanumérico? ', x.isalnum())
print('O que foi digitado é alfabético? ', x.isalpha())
print('O que foi digitado é um número? ', x.isnumeric())
print('O que foi digitado está em MAIÚSCULA? ', x.isupper())
print('O que foi digitado está em minúscula? ', x.islower())
print('O que foi digitado está capitalizado? ', x.istitle())
