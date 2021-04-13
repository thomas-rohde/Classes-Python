n = s = 0
while True:
	n = int(input('Insira um nº'))
	if n == 999:
		break
	s += n
print(f'A soma vale {s}')