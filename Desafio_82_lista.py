galera = list()
dado = list()
r = 'S'
totmai = totmen = 0
while r == 'S':
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    r = str(input('Voce quer continuar?[S/N]')).upper()
for p in galera:
    if p [1] >= 80:
        totmai+=1
    else:
        totmen+=1
print(f'Temos {totmai} pessoas obesas e {totmen} pessoas magras')

