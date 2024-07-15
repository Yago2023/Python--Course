dados = dict() #criando um dicionario 
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])
print(dados['idade'])
del dados['idade']
filme = {'titulo' :'Star Wars', 'Ano': 1977 , 'Diretor':'George Lucas'}
'''print(filme.values()) #mostra todos os valores 
print(filme.keys()) #mostra todas as Keys "numero de posições"
print(filme.items()) #mostra todos os values and keys juntos '''

for k,v in filme.items():
    print(f'O key {k} é valor:{v}')