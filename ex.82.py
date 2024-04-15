valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]')).upper()
    if r in 'N':
         break
for i,v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {valores}')
print(f'A lista com apres é {pares}')
print(f'A lista com impares é {impares}')