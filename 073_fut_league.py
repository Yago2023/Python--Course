time = ('Palmeiras','Flamengo','Cruzeiro','Internacional','Fluminense',
        'Corinthians','Athletico-PR','Atlético','Fortaleza','São Paulo',
        'América','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Grêmio','Vasco','Bahia')
print(f'Lista do time do brasileirão:{time}')
print('Os cinco primeiros colocados são: ')
for cont in range (0,5):
    print(time[cont])
print('Os ultimos colocados são: ')
for cont in range(-5,0):
    print(time[cont])
print(f'Essa é a lista em ordem alfabetica: {sorted(time)}')

for pos, times in enumerate(time, 1):
    if times == 'Santos':
        print(f'O Santos está na posição {pos}')
        break

