def notas(*n, sit=False):
    """
    -> Função: analisar os boletins de vários alunos
    :param n: as notas
    :param sit: se deseja ver ou não a situação do aluno
    :return: dicionário com dados do boletim
    """
    r0 = dict()
    r0['total'] = len(n)
    r0['maior'] = max(n)
    r0['menor'] = min(n)
    r0['média'] = sum(n) / len(n)
    if r0['média'] >= 7:
        r = 'APROVADO'
    elif r0['média'] > 3:
        r = 'RECUPERAÇÃO'
    else:
        r = 'REPROVADO'
    if sit:
        r0["situação"] = r
    return r0


#MAIN
resp = notas(5.5, 3.5, 1, 1.5, sit=True)
print(resp)