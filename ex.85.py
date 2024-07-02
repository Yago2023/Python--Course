lista = list()
par = list ()
impar = list()
cont = 0
for c in range(0, 7):
    cont += 1  # Correção aqui
    lista.append(int(input(f'Digite {cont}º valor: ')))
print(lista)
for p in (lista): #check se é par
    if p % 2 == 0:
        par.append(lista[:])
    else: # se não é par, por regra é impar 
        impar.append(lista[:])
    print(par)
    print(impar)