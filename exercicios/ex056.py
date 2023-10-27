idmedia = 0
totidade = 0
idhmv = 0
hmv = ''
midf = 0
tot20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '.format(p))).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    totidade += idade
    if p == 1 and sexo == 'M':
        idhmv = idade
        hmv = nome
    if sexo == 'M' and idade > idhmv:
            idhmv = idade
            hmv = nome
    if sexo =='F' and idade < 20:
        tot20 += 1       
idmedia = totidade / 4
print('A média de idade do grupo é de {} anos.'.format(idmedia))
print('O homem mais velho do grupo é o {}, com {} anos de idade.'.format(hmv, idhmv))
print('Este grupo contém {} mulher(es) com menos de 20 anos de idade.'.format(tot20))
