num = int(input('Digite um número inteiro: '))
print(''''Escolha uma opção de conversão
[1] Para Hexadecimal
[2] Para Octal
[3] Para Binario''')
opcao = int(input('Escolha uma opcao:'))
if opcao == 1:
    print('O numero {} convertido para Exadecimal é: {}'.format(num, hex(num)[2:]))
elif opcao ==2:
    print('O numero {} convertido para Octal é: {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O numero {} convertido para Binario é:{}'.format(num,bin(num)[2:]))
else:
    print('A opcao é invalida')
