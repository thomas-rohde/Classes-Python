from random import randint
n = (randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100))
print(f'''Os valores sorteados foram {sorted(n)},
O maior nº gerado foi {max(n)}, enquanto o menor foi {min(n)}''')