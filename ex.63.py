print("-"*30)
print("Sequencia de Fibonacci")
print('-'*30)
n = int(input('Digite um numero para a sequencia de Fibonacci: '))
n1 = 0
n2 = 1
c = 0
print('{} -> {} -> '.format(n1,n2),end= "")
while c < n:
    n3 = n1 + n2
    print('{} -> '.format(n3),end="")
    c += 1
    n1 = n2
    n2 = n3
print("FIM")

