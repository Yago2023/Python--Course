#Mostra uma mesma lista dividida em duas listas internas de pares e impares
lista = [[], []]
valor = 0
cont = 0
for c in range(0, 7):
    cont += 1  # Correção aqui
    valor = int(input(f'Digite {cont}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
print(lista)
lista[0].sort() 
lista[1].sort()
print(f'Os pares listados são {lista[0]}')
print(f'Os Impares listados são {lista[1]}')
 