s = 0
s0 = 0
for três in range(0, 501, 3):
    if três % 2 != 0:
        print(três, end='/ ')
        s += três
        s0 += 1
print('\nA soma desses {} valores solcitados é {}'.format(s0, s))