t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezessete', 'dezoito', 'desenove', 'vinte')
while True:
    n = int(input('Digite um nº entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Dado inválido, tente novamente')
print(f'você digitou o nº {t[n]}')