# desafio 71
print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('='*30)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        total += 1
    else:
        print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

