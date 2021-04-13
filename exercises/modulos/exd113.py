def leianum(msg):
    while True:
        if x == 0:
            try:
                i = int(input(msg))
            except (ValueError, TypeError):
                print(f'\033[31mERRO! Digite um nº {tipo[x]}\033[m')
            except (KeyboardInterrupt):
                i = 0
                print('Usuario preferiu não informar um nº')
                return i
            else:
                return i
        else:
            try:
                r = float(input(msg))
            except (ValueError, TypeError):
                print(f'\033[31mERRO! Digite um nº {tipo[x]}\033[m')
            except (KeyboardInterrupt):
                print('Usuário preferiu não informar um nº')
                r = 0
                return r
            else:
                return r


#MAIN
tipo = ['inteiro', 'real']
n = list()
for x in range(0, 2):
    n.append(leianum(f'Digite um nº {tipo[x]}: '))
print(f'O nº {tipo[0]} digitado foi {n[0]}, enquanto o nº {tipo[1]} foi {n[1]}')