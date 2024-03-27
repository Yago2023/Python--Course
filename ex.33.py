num = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite mais um número: '))
#'verificando que é o menor'
menor = num
if num2 < num and num2 < num3:
    menor = num2
    if num3 < num and num3 < num2:
        menor = num3
#'verifcando quem é o maior'
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print('O menor valor digitado é o {}'.format(menor))
print('O maior valor digitado é o {}'.format(maior))
