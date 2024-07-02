galera = list()
dado = list()
lista_maior = list()
lista_menor = list ()
r = 'S'
totmai = totmen = qto = 0
while r == 'S':
    qto += 1
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        totmai = totmen = dado[1]
    else:
        if dado [1] > totmai:
            totmai = dado [1]
        if dado [1] < totmen:
            totmen = dado [1]
    galera.append(dado[:])
    dado.clear()
    r = str(input('Voce quer continuar?[S/N]')).upper()
print ('-='*30)
print(f'Temos um total de {qto} pessoas cadastradas na lista')
print(f'O maior pesoa foi de {totmai}kg. Pedo de ',end='')
for p in galera:
    if p[1] == totmai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor pedo foi de {totmen}kg. Pedo de ', end='')
for p in galera: 
    if p[1] == totmen:
        print(f'[{p[0]}]',end='')
print()
