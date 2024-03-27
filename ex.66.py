# Ex: 66 Somador
n = s = x = 0
while True:
    n = int(input('Digite um numero: (999 para parar)'))
    if n == 999:
        break
    s += n
    x += 1
print(f'A soma vale {s} e voce digitou {x} numeros')