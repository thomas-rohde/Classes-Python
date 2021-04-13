n = x = c = 0
while True:
    n = int(input('Insira um nº(0 cancela as operações): '))
    if n == 0:
        break
    x += n
    c += 1
print(f'A soma de {c} nºs deu {x}, tenha um bom dia!')
