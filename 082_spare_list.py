#Pega valores de uma lista e divide em outras duas listas, uma par e uma impar
valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: '))) #entrada com valores  a lista
    r = str(input('Quer continuar? [S/N]')).upper()
    if r in 'N':
         break
for i,v in enumerate(valores): #check se é par
    if v % 2 == 0:
        pares.append(v)
    else: # se não é par, por regra é impar 
        impares.append(v)
print('-='*30) #printar as 3 listas 
print(f'A lista completa é {valores}')
print(f'A lista com apres é {pares}')
print(f'A lista com impares é {impares}')