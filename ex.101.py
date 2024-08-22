def voto(v=0):
    x = 2024 - v
    if x < 16:
        print('Voto negado')
    elif 16 < x < 60:
        print('Voto Obrigatorio')
    elif x >= 60:
        print('Voto opcional')
    else:
        print('Voto negado')


idade = int(input('Digite o ano que voce nasceu: '))
print(voto(idade))
