x = ()
for cont in range (0,4):
    num = int(input('Digite um numero: '))
    x += (num,)
teste09 = 0
for number in x:
    if number ==9:
        teste09 += 1
print(f'O numero 9 apareceu {teste09} vezes')

for pos, num in enumerate(x,1):
    if num == 3:
        print(f'O numero 3 está na posição {pos}')
        break
    else:
        print('Voce não tem numeros 3')
        break
pares=0
for num in x:
    if num % 2 == 0 :
        pares += 1 
print(f'Voce tem {pares} mumeros pares')