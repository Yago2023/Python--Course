def ficha (jog = '<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else: 
    ficha(n ,g)