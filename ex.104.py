def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número interio válido')
        if ok:
            break

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número: {valor}')
    

    