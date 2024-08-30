def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('Erro! Digite um número interio válido')

    return valor

#programa principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número: {n}')
    

    