# Ex: 67 tabuada
from colorama import init, Fore
while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n < 0:
         break
    for c in range (1, 11):
        print ('{:.0f} x {} = {:.0f}'.format(n ,c ,n*c))
print(Fore.RED + 'Voce digitou um numero negativo e o programa encerrou' + Fore.RESET)