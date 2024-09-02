def voto(v=0):
    from datetime import date #importar aqui economiza memoria
    date = date.today().year
    x = date - v
    if x < 16:
        return f'Voto negado'
    elif 16 <= x < 18 or x > 65:
        return f'Voto Opcional'
    else:
        return f'Voto Obrigatorio'


idade = int(input('Digite o ano que voce nasceu: '))
print(voto(idade))
