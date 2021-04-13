tc = float(input('A temperatura atual em ºC é '))
tk = tc + 273
tf = 9 * tc / 5 + 32

print('Convertendo {:.2f}ºC, resultamos em {:.2f}ºF e {:.2f}K'.format(tc, tf, tk))
