from datetime import date


def voto(ano):
    ano0 = date.today().year
    a = ano0 - ano
    if a < 16:
        return f'Com {a} anos: NÃO VOTA'
    elif 16 <= a < 18 or a > 65:
        return f'Com {a} anos: VOTO OPCIONAL'
    else:
        return f'Com {a} anos: VOTO OBRIGATÓRIO'


#MAIN
ano1 = int(input('Em que ano você nasceu? '))
print(voto(ano1))