
#tupla = tuple(random.randint(1,20))
'''for tupla in range (0,6):
    tupla = tuple(random.randint(1,20))
    print(tupla)'''
from random import randint
x = (randint(1,10),randint(1,10),randint(1,10),
     randint(1,10),randint(1,10))
print('Valores sorteados foram: ',end='')
for n in x:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(x)}')
print(f'\nO menor valor sorteado foi {min(x)}')




