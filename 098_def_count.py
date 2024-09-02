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


def contador1(i,f,p):
    print(f'O inicio da contagem {i} o final {f} com passe de {p}')
    if p < 0:
        p*=-1
    if p ==0:
        p=1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -=p
        print('FIM')



#programa principal
print(contador1(1,10,1))
print(contador1(10,0,2))
print('Agora é sua vez de personalizar sua contage: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passe: '))
contador1(ini,fim,pas)

