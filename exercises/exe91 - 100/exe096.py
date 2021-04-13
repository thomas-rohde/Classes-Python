def escreva(txt):
    x = int(len(txt) + 4)
    print('~' * x, f'\n  {txt}')
    print('~' * x)

while True:
    txt0 = str(input('Escreva algo interessante: '))
    escreva(txt0)
    r = str(input('Quer Continuar? [S/N] '))
    if r in 'Nn':
        break