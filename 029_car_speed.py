num = float(input('Digite a velocidade do carro: '))
x = (num - 80) * 7
if num <= 80:
    print('Sua velocidade está no permitido')
else:
    print ('Voce passou a velocidade e sua multa é de R${:.2f} reais'.format(x))
