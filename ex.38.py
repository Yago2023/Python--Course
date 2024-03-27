num = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))

if num > num2:
    print('o PRIMEIRO é maior'.format(num,num2))
elif num < num2:
    print ('o SEGUNDO é maior'.format (num,num2))
else:
    print('Os valores são iguais')
