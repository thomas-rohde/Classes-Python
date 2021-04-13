def aumentar(preço=0, taxa=0, formato=False):
    r = (preço * taxa / 100) + preço
    return r if not formato else moeda(r)


def diminuir(preço=0, taxa=0, formato=False):
    r = preço - (preço * taxa / 100)
    return r if formato is False else moeda(r)


def dobro(preço=0, formato=False):
    r = preço * 2
    return r if not formato else moeda(r)


def metade(preço=0, formato=False):
    r = preço / 2
    return r if formato is False else moeda(r)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo (preço, aumento0, redução0, f=True):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço:\t\t{dobro(preço, f)}')
    print(f'Metade do preço:\t{metade(preço, f)}')
    print(f'{aumento0}% de aumento:\t\t{aumentar(preço, aumento0, f)}')
    print(f'{redução0}% de redução:\t\t{diminuir(preço, redução0, f)}')
    print('-' * 30)