from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
x = atual - nasc
if x <= 9:
    print('Voce está na categoria Mirim')
elif x <= 14:
    print('Voce está na categoria Infantil')
elif x <= 19:
    print('Voce esta na categoria Junior')
elif x <= 25:
    print('Voce esta na cateria Senior')
else:
    print('Voce está na categoria Master')