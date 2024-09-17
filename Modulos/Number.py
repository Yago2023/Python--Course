import uteis


n = float(input('Digite o numero:  '))
print(f'O dobro de {n} é R${uteis.dobro(n)}')
print(f'A metade de {n} é R${uteis.metade(n)}')
print(f' 10% desse valor é R${uteis.aumentar(n)}')
print(f'13% desse valor é R$ {uteis.diminuir(n)}')