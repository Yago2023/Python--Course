lista = [[],
         [],
         []]
cont = 0
for c in range(0,9):
    valor = int(input('Digite o valor:'))
    cont += 1
    if cont <= 3:
        lista[0].append(valor)
print(lista)
    
    
