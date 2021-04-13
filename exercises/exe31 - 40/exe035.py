n = int(input('Digite um nº inteiro: '))
print('''Escolha uma das basses para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('\033[4;31m{}\033[m convertido para BINÁRIO é igual a \033[4;31m{}\033[m'.format(n, bin(n)[2:]))
elif opção == 2:
    print('\033[4;31m{}\033[m convertido para OCTAL é igual a \033[4;31m{}\033[m'.format(n, oct(n)[2:]))
elif opção == 3:
    print('\033[4;31m{}\033[m convertido para HEXADECIMAL é igual a \033[4;31m{}\033[m'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente')