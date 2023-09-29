nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('A média do aluno foi de {:.1f} pontos, aluno \033[1;31mREPROVADO!\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('A média do aluno foi de {:.1f} pontos, aluno em \033[1;33mRECUPERAÇÃO!\033[m'.format(media))
else:
    print('A média do aluno foi de {:.1f} pontos, aluno \033[1;32mAPROVADO!\033[m'.format(media))
