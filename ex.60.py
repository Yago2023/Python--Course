x = int(input('Digite um numero que voce deseja saber o fatorial: '))
c = x
fat = 1
print('calculando {}! = '.format(x), end='')
while c > 0 :
    print('{} '.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))



