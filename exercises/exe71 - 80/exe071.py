times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
         'Athletico-PR', 'Santos', 'Corinthians')
print(f'''{times}

{sorted(times)}

{times[:5]} - {times[6:]}

{len(times)}
Athletico-PR está na {times.index("Athletico-PR")+1} posição''')