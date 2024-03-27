n = int(input('Digite um número de até 4 dígitos: '))
un = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10

print('Analisando o número: {} '.format(n))
print('Unidade: {} '.format(un))
print ('Dezena: {} '.format(dez))
print('Centena: {} '.format(cen))
print('Milhar: {} '.format(mil))