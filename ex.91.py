from random import randint
x = 1
jogadores = dict()
jog = []
for c in range (4):
    jogadores[f'jogador {c+1}: '] = randint (0, 10)
    jog.append(jogadores.copy())
print(jog)