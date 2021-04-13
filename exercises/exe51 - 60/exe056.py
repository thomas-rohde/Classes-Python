from random import randint
ia = int(randint(0,10))
pc = int(11)
count = 0
print('\033[7m-', '\033[7m Vamos Jogar! -\033[m' * 5, '\nAdivinhe o número em que estou pensando')
print('\033[7m-\033[m' * 77)
while ia != pc:
    count += 1
    pc = int(input('Digite um nº entre 0 e 10: '))
    if pc != ia:
        print('\033[1;31mVOCÊ ERROU\033[m, tente novamente, mas antes...')
        if pc < ia:
            print('vou te dar uma dica, é maior')
        else:
            print('vou te dar uma dica, é menor')
print('Parábens, você adivinhou meu nº, demorou {} tentativa(s)'.format(count))