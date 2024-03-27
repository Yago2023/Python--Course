salario = float(input('Digite o salário: '))
if salario < 1250:
    x = salario * 0.10
else:
    x = salario * 0.15
print( 'Para quem ganhava R${} após o aumento é de: R${} reais'.format(salario,x+salario))

