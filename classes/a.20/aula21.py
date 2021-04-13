def mensagem(txt):
    """
    -> Mostra um texto com linhas bem s2
    :param txt: texto entre linhas
    :return: sem retorno
    criado por -Thomas Rohde-
    """
    print('-=-' * 10)
    print(txt)
    print('-=-' * 10)


help(mensagem)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


soma = list()
soma.append(somar(c=4, b=1))
soma.append(somar())
print(soma)