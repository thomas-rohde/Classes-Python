p = str(input('Digite uma frase:')).strip().upper()
p0 = p.split()
junto = ''.join(p0)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
