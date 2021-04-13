from random import randint
from time import sleep


def sorteia(list):
    for c in range(0, 5):
        list.append(randint(1, 10))
    for c in list:
        print(c, end=' ')
        sleep(0.5)

def somaPar(list0, par):
    for c in list0:
        if c % 2 == 0:
            par += c
    print(f'-> A soma de nºs pares dá : {par}')



#MAIN:
números = []
sorteia(números)
somaPar(números, 0)