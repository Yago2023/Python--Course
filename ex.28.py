import random
num = random.randint(1,5)
x = int(input('Pense em um número entre 1 e 5 e digite: '))
if x == num:
    print('Voce acertou')
else:
    print('Voce errou.')
print(num)
