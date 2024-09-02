casa = float(input('Qual o valor da casa que voce deseja compra?'))
sal = float(input('Qual o valor do seu salario?'))
div = int(input('Em quantOS anos voce deseja dividir esse valor?'))

x = casa / (div * 12)
y = 0.30 * sal
if x <= y:
    print('Para pagar uma casa de R${:.2f}Voce vai pagar R${:.2f} por {} anos'.format(casa,x,div))
else:
    print('emprestimo negado')


