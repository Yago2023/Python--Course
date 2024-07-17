#Retirando dados de uma Matriz
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = colun = linh = 0
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c] = int(input(f'Digite o valor para [{l}, {c}]: ' ))
print('-='*30)
print('MATRIZ')
for l in range (0,3):#para mostar na tela
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 ==0:
            par += matriz[l][c]
    print()
print('-='*30)
print(f'A soma de todos os valores pares é {par}')
for l in range (0,3):
    colun += matriz[l][2]
print(f'A soma da terceira coluna é {colun}')
for c in range(0,3):
     if c == 0:
        linh = matriz[1][c] 
     elif matriz[1][c] > linh:
         linh = matriz[1][c]
         
print(f'O maior número da segunda linha é {linh}')
