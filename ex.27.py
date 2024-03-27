nome = input(str('Digite o seu nome completo: ')).strip()
x = nome.split()
print('O seu primeiro nome é:{}'.format(x[0]))
print('O seu último nome é: {}'.format(x[len(x)-1]))

