print('-=-'*10)
print('Analisandor de Triângulos')
print('-=-'*10)
t0 = float(input('Primeiro segmento: '))
t1 = float(input('Segundo segmento:' ))
t2 = float(input('Terceiro segmento:' ))
#Fundamento dos triângulos===================================
if t0<t1+t2 and t1<t0+t2 and t2<t0+t1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    # Qual triângulo é---------------------------------------
    if t0 == t1 == t2:
        txt = str('\033[7;31mEQUILÁTERO\033[m')
    elif t0 == t1 or t0 == t2 or t1 == t2:
        txt = str('\033[7;33mISÓSCELES\033[m')
    else:
        txt = str('\033[7;35mESCALENO\033[m')
    # TEXTO--------------------------------------------------
    print('Esse triângulo é {}'.format(txt))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
