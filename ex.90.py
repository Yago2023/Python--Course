situacao = dict()
situacao ['nome'] = str(input('Digite o nome do aluno: '))
situacao ['nota'] = int(input(f'Digite a media de {situacao["nome"]} : '))
print(f'Média é igual a de {situacao["nome"]} é {situacao["nota"]} ')
if situacao['nota']>=6:
    print(f'Aluno Aprovado')
    situacao['final']= 'aprovado'
else:
    print('Aluno Reprovado')
    situacao['final']= 'Reprovado'
print(situacao)