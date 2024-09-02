frase = input(str('Digite uma frase qualquer: ')).upper().strip()
print('Na frase tem {} letras A'.format(frase.count('a')))
print('A primeira letra apareceu em: {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))


