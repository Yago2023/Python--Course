'''dados = dict() #criando um dicionario 
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])
print(dados['idade'])
del dados['idade']
dados['peso'] = 99
filme = {'titulo' :'Star Wars', 'Ano': 1977 , 'Diretor':'George Lucas'}'''
'''print(filme.values()) #mostra todos os valores 
print(filme.keys()) #mostra todas as Keys "numero de posições"
print(filme.items()) #mostra todos os values and keys juntos '''

'''for k,v in filme.items(): #items tenho que colocar key and value/caso não queira é só colocar .keys or .values
    print(f'O key {k} é valor:{v}')

for k in filme.keys():
    print(k)
'''
''' #colocar uma lista dentro de um dicionario 
brasil = []
estado1 = {'uf': 'Goias', 'sigla' : 'GO'}
estado2 = {'uf': 'São Paulo', 'sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
'''
estado = dict ()
brasil = ()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
