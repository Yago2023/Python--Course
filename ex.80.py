#lista ordenada sem repetições - importançia do sort
lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]: #Se o numero for maior que o numero que está no ultimo elemento (len de lista)
        lista.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0 #começa na posição 0 
        while pos < len (lista): #check até ultima posição 
            if num <= lista[pos]: #verifica se num que vai inserir se é menor ou igual
                 lista.insert(pos,num) #na posição pos valor n 
                 print(f'adicionado na posição {pos} da lista')
                 break
            pos += 1 # passa pra próxima posição 
print('-=' *30)
print(f'Valores da lista ditador em ordem foram {lista}')



