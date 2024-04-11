valores = []
r = 'S'
while r == 'S':
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    r = str(input('Quer continuar? [S/N]')).upper()
valores.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(valores)} valores na lista')
print(f'A lista em ordem descrescente é {valores}')
if 5 in valores:
    print('O valor 5 se encontra na lista')
else:
    print('O valor 5 não se encontra na lista')