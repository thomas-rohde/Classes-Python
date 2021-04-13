boletim = []
notas = []
r0 = 0
while True:
    notas.append(str(input('Nome: ')))
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    notas.append((notas[1] + notas[2]) / 2)
    boletim.append(notas[:])
    notas.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print('-' * 20 ,'No. NOME       MÉDIA\n', '-' *20)
for i in range(0, len(boletim)):
    print(f'{i:<3}{boletim[i][0]:<12}{boletim[i][3]}')
while True:
    r0 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r0 == 999:
        break
    if r0 < len(boletim):
        print(f'Notas de {boletim[r0][0]} são {boletim[r0][1]} e {boletim[r0][2]}')
print('Tenha um bom dia!')