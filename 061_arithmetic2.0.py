pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite o numero da razao'))
c = 0
termo = pri
while c <= 10:
    print('{} -> '.format(termo), end ='')
    termo += raz
    c += 1
print('FIM')
