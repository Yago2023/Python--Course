num = float(input('Digite a distancia da sua viagem: '))
if num <=200:
   x = 0.50 * num
else:
   x = 0.45 * num
print("A sua viagem vai ficar em: R${:.2f} ".format(x))