def area(a,b):
    area = a * b
    print(f'O terreno tem largura de {a} e comprimento de {b} o total é {area}')
    

print('Controle de terrenos')
print('-='*20)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
print(area(a,b))