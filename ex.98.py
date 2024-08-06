from time import sleep
def contador():
    print('=-'*10)
    print('Contagem de 1 até 10 em 1 em 1')
    for x in range(1,11,1):
        print(x,end=' ')
    print('FIM')
    print('=-'*10)
    sleep(3)
    print('=-'*10)
    print('Contagem de 10 até 0 em 2 em 2')
    for y in range(10,-1,-2):
        print(y,end=' ')
    print('FIM')
    print('=-'*10)
    sleep(3)
    print('=-'*10)
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    for w in range(inicio,fim,passo):
        print(w,end=' ')
    print('=-'*10)


print(contador)