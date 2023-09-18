import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o último nome: ')
lista = [n1, n2, n3, n4]
sort = random.choice(lista)
print('O nome do aluno escolhido para apagar o quadro é: ', sort)
