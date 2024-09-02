nome = str(input('Digite o seu nome: ')).strip()

print('O seu nome em maiusculo é: {} '.format(nome.upper()))
print('O seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
