#Versão Melhorada exe040

print('-=-'*10)
print('Analisandor de Triângulos')
print('-=-'*10)
t0 = float(input('Primeiro segmento: '))
t1 = float(input('Segundo segmento:' ))
t2 = float(input('Terceiro segmento:' ))
#Fundamento dos triângulos
if t0<t1+t2 and t1<t0+t2 and t2<t0+t1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')