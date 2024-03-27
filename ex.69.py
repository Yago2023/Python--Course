# ex. 69
while True:
    sexo = again = 'x'
    homem = mulher = 0
    idade = int(input('Digite a idade da pessoa:'))

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]')).strip().upper()[0]
        if sexo == 'M' and idade >= 18:
            homem += 1
        elif sexo == 'F' and idade < 20:
            mulher += 1
    while again not in 'YN':
        again = str(input('Quer continuar? [Y/N]')).strip().upper()[0]
        if again == 'N':
            break
    if again == 'N':
        break
print(f'Voce finalizou e tem um total de {homem} com mais de 18 anos e {mulher} com menos de 20 anos')