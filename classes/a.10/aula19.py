pessoas = {'nome': 'Thomas', 'sexo': 'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
pessoas["nome"] = 'Leo'
pessoas["peso"] = 98
print()
for x, y in pessoas.items():
    print(f'{x} = {y}')