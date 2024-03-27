from datetime import date
atual = date.today().year
num = int(input('Digite o ano de nascimento: '))
x = atual - num
if x < 18:
    print('Voce irá se alistar em {}'.format(num+18))
elif x > 18:
    print('Voce devia ter se alistado no ano {}'.format(num+18))
else:
    print('Voce se alista esse ano')
