n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
o: int = 0
while 5 != o:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    o = int(input('Sua escolha: '))
    if o == 1:
        print('>>>', n1 + n2)
    elif o == 2:
        print('>>>', n1 * n2)
    elif o == 3:
        if n1 > n2:
            print('>>>O maior nº é ', n1)
        elif n1 == n2:
            print('>>>São Iguais')
        else:
            print('>>>O maior nº é ', n2)
    elif o == 4:
        print('>>>Digite novos valores: ')
        n1 = input('>>>>Primeiro Valor:')
        n2 = input('>>>>Segundo Valor: ')
    print('-=-' * 8)
print('Fim do Programa, Volte Sempre!')