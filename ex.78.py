'''existem dois modos que foi feito'''
'''x = []
for cont in range (0,5):
    num = int(input('Digite um numero: '))
    x.append(num)
print(x)
maior = max(x)
menor = min(x)
for pos,valor in enumerate(x):
    if valor == maior:
        print(f'O maior valor foi de: {maior} e está na posição {pos}')
    if valor == menor:
        print(f'O menor valor foi de: {menor} e está na posição {pos}')'''
listanum = []
maior = 0
menor = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum [c] > maior:
            maior = listanum[c]
        if listanum [c] < menor:
            menor = listanum [c]
print('-'*30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print('f{i}...', end='')
print()
print(f'O menor valor digitado foi{men} nas posições', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...'end='')
    print()