camp = {}
gols = []
camp ['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas jogou: '))
for x in range(0,partidas):
    x = int(input(f'Gols partida {x}: '))
    gols.append(x)
    camp['gols'] = gols
soma = sum(gols)
camp['total'] = soma
print(30*'-=')
print(camp)
print(30*'-=')
for v,k in camp.items():
    print(f'O campo {v} tem valor {k}')
print(30*'-=')
print(f'O jogador{camp["Nome"]} jogou {partidas} partidas')
