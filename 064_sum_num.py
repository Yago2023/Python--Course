n1 = int(input('Digite um número para ser somado (digite 999 para encerrar): '))
soma = 0
while n1 != 999:
    soma += n1
    n1 = int(input('Digite mais um número (digite 999 para encerrar): '))
    print("-" * 30)
print('A soma de todos os números digitados é igual a: {}'.format(soma))
print('FIM')
