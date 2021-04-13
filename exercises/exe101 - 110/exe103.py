def leiaint(p):
    while True:
        r = str(input(p))
        if r.isnumeric():
            return r
        else:
            print('\033[31mERRO! Digite um nº, inteiro válido\033[m')


#MAIN
n = leiaint('Digite um nº: ')
print(f'Você acabou de digitar o nº {n}')