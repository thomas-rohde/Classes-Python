f = str(input('Digite uma frase: ')).strip()
a = f.lower()
print('''A sua frase possuí {} letras A
Ela aparece primeiramente na posição {}
e sua último local é {}'''
.format(a.count('a'), a.find('a') + 1, a.rfind('a') + 1))