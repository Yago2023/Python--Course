from datetime import datetime
dados = {}
dados ['Nome'] = str(input('Digite o seu nome: '))
nasc = int(input('Ano de Nascimento: '))
dados ['Idade'] = datetime.now().year - nasc
dados ['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano da contratação: '))
    dados ['Salario'] = int(input('Salario RS: '))
    dados['Aposentadoria'] = ((dados['Contratação']+ 35) - datetime.now().year)
print(dados)
for k,v in dados.items():
    print(f'{k} : {v}')
