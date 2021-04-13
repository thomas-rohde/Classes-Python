def maior(* n):
    m = 0
    print('-=' * 30)
    print('Analizando os valores informados...')
    for c, v in enumerate(n):
        print(v, end=' ')
        if v > m or c == 1:
            m = v
    print(f'Foram informados {len(n)} valores ao todo,\nsendo o maior deles {m}.')


#MAIN
maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()