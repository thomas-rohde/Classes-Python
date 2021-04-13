palavras = ('Abacate', 'Caixa', 'Seguro', 'Ressucita', 'Gostosa', 'Ficante')
for p in palavras:
    print(f'A palavra {p.upper()}  tem como vogais', end=' ')
    for letra in p.lower():
        if letra in 'aeiou':
            print(letra, end=' ')
    print('')