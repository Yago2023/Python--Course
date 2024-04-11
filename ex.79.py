#programa que adiciona valores a uma lista, sem repetir e pergunta usuario se deseja continuar
valores = []
r = 'S'
while r == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in valores: 
        valores.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...') 
    r = str(input('Quer continuar? [S/N]')).upper()
valores.sort()
print(valores)
    
