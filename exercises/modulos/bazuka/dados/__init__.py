def validador(r, r0=0):
    while True:
        r = str(input('Digite o preço: R$')).strip().replace(',', '.')
        if r.isalpha() or r == '':
            print(f'\033[0;31mERRO! \"{r}\" é inválido, tente novamente\033[m')
        else:
            r0 = float(r)
            break
    return r0