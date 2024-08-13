'''def soma (a,b):
    s= a +b
    print(f'A soma de {a} com {b} é igual a {s}')


#Programa principal - deve pular 2 linhas 
soma(6,5)
soma(2,5)
'''
#empacotamento
#def contador (*núm); #independente do tanto de parâmetro vai jogar tudo em num
#	for valor in num:
#		print(f'{valor} ', end='')
#	print('FIM!')
	
'''
def dobra(lst)
	por = 0 
	while pos<len(lst):
	   lst[pos]*=2
	pos +=1

valores = [6,3,9,1,0,2]
dobra (valores)
print (valores)'''


#help()
#print(input.__doc__)
#docstrings colocar descrição abre 3 aspas e escreve um texto para que apareça no help 
#Parametros opcionais - decidir e não usar todos os valores def somar (a=0,b=0,c=0):
#escopo de variaveis - variavel local e variavel global 

def teste(b):
    b+=4
    c = 2 
    print(f'A dentro vale {a}')
    print(F'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5 

print(teste(b))