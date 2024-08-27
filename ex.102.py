def fatorial (num=1,show=False):
    ''''
    -> Calcule o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostre ou não a conta
    :return: O valor do Fatorial de um pumero n.
    '''
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ' , end='')
        f *= c
    return True

help(fatorial)