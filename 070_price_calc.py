# ex. 70
total = alto = menor = cont = barato = 0
while True:
    produto = str(input('Digite o produto: '))
    preco = float(input('Digite o valor do produto : '))
    total += preco
    cont += 1
    if preco > 1000:
        alto += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    again = ' '
    while again not in 'YN':
        again = input('Quer continuar? [Y/N]').strip().upper()[0]
        if again not in 'YN':
            print('Opção inválida. Por favor, digite Y para sim ou N para não.')
    if again == 'N':
        break
print(f'Programa finalizado, a soma dos produtor foram {total} o valor do produto mais caro foi de {menor} que é o {barato}')
print(f'Voce tem {alto} produtos a cima de 1000 reais')