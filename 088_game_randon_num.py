from random import randint
import time
jogos = list()
lista = list()

quant = int(input('Quantos numeros quer sortear: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear ()
    tot +=1
print(f'Sorteando {quant} Jogos')
for i,l in enumerate(jogos):
    print(f'Jogo:{i+1}: {l}')
    time.sleep(2)
