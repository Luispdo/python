#print(input.__doc__)
#help(input)

def contador(i, f, p):
    """Faz uma contagem e mostra na tela.

    Args:
        i (parametro): início da contagem
        f (parametro): fim da contagem
        p (parametro): passo da contagem
    
    Retorno:
        Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
    
    
contador(2, 10, 2)
help(contador)
