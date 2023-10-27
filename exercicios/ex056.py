idmedia = 0
totidade = 0
idhmv = 0
for p in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M para masculino e F para feminino): ')).upper()
    totidade = totidade + idade
    if sexo == 'M':
        idhmv = idade
        hmv = 'nome'
        if idade > idhmv:
            idhmv = idade
            hmv = 'nome'
            print(hmv)
idmedia = totidade / 4
print(idmedia)
