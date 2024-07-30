#Digite nome e peso de pessoas e vamos mostrar os mais pesados e leves e o tamanho da lista 
galera = list()
dado = list()
lista_maior = list()
lista_menor = list ()
r = 'S'
totmai = totmen = qto = 0
while r == 'S': #Coloca um continua ou não para o usuario 
    qto += 1 #Contador para verificar quantas pessoas tem na lista 
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0: #Verificação se lista está vazia 
        totmai = totmen = dado[1]
    else:
        if dado [1] > totmai: #verificação qual é maior 
            totmai = dado [1]
        if dado [1] < totmen: #verificação qual é menor 
            totmen = dado [1]
    galera.append(dado[:])
    dado.clear()
    r = str(input('Voce quer continuar?[S/N]')).upper()
print ('-='*30)
print(f'Temos um total de {qto} pessoas cadastradas na lista')
print(f'O maior peso foi de {totmai}kg. Peso de ',end='')
for p in galera: #verifica valores se forem = a maior ele printa o nome dessa pessoa 
    if p[1] == totmai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {totmen}kg. Peso de ', end='') #verifica valores se forem = a menor ele printa o nome da pessoa
for p in galera: 
    if p[1] == totmen:
        print(f'[{p[0]}]',end='')
print()
