from random import randint
v = 0
while True:
    n = int(input('Digite um valor: '))
    aleatorio = randint(0, 10)
    soma = aleatorio + n
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador {aleatorio}. Total de {soma} ',end = '')
    print('Deu Par' if soma % 2 == 0 else 'Deu Impar')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    elif (escolha == 'I'):
        if soma % 2 == 1:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos joga novamente? ')
print(f'GAME OVER! Voce jogou {v} vezes')