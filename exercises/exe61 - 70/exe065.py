while True:
    n = int(input('Insira um nº e veja sua tabuada ! '))
    print('=' * 15)
    if n <= 0:
        break
    for t in range(1, 11):
        print(f'{n} X {t} = {n * t}')
    print('=' * 15)
print('Acabou, tenha um bom dia!')
