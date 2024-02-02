def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.

    Args:
        n (param): O número a ser calculado.
        show (param. lógico, (optional)): Mostrar (True) ou não (False) a conta. Padrão é False.

    Returns:
        valor inteiro: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, True))
help(fatorial)
