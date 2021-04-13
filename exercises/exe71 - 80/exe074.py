produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for posi in range(0, len(produtos)):
    if posi % 2 == 0:
        print(f'{produtos[posi]:.<30}', end='R$ ')
    else:
        print(f'{produtos[posi]:0>6.2f}')