from time import sleep


def crescente(com, fim, inter):
    if inter < 0:
        inter *= -1
    for count in range(com, fim + 1, inter):
        print(count, end=' ')
        sleep(0.7)
    print()


def decrescente(com, fim, inter):
    if inter > 0:
        inter *= -1
    for count in range(com, fim - 1, inter):
        print(count, end=' ')
        sleep(0.7)
    print()


#Main
crescente(0, 10, 1)
print('-' * 30)
decrescente(10, 0, 2)
print('=' * 30, '\nAGORA É A SUA VEZ!!!\n', '-' * 15)
c = int(input('Onde você quer começar? '))
print('-' * 15)
f = int(input('Onde você quer terminar? '))
print('-' * 15)
i = int(input('Qual serão os intervalos? '))
print('-' * 30)
print('Calculando...')
print('-' * 30)
sleep(1)
if c < f:
    crescente(c, f, i)
elif c > f:
    decrescente(c, f, i)
print('-' * 30)
print('Fim! Tenha um bom dia!')