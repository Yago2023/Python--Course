import random
num = random.randint(1,5)
x = -1
y = 0
print(num)
while x != num:
    x = int(input("Tente acertar o numero que voce pensou: "))
    y += 1
print("Parabéns voce acertou, foi necessário {} vezes para chegar ao valor correto ".format(y))
