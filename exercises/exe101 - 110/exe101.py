from math import factorial


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um nº
    :param n: O nº a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial do nº
    """
    r = 1
    if show:
        for c in range(n, 0, -1):
            print(f'{c}', end=' ')
            if c != 1:
                print('x', end=' ')
            r *= c
        return f'= {r}'
    else:
        return factorial(n)


#MAIN
print(fatorial(5, True))
print(fatorial(5))
help(fatorial)