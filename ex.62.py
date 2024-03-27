pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite o numero da razao'))
termo = pri
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end ='')
        termo += raz
        c += 1
    print('PAUSA')
    mais = int(input('Voce deseja ver mais quantos termos? '))
print('FIM')