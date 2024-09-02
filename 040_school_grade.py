nota = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota + nota2) / 2

if media < 5.0:
    print('Sua média é {} e voce está REPROVADO'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua media é {} e voce está de RECUPERAÇÃO'.format(media))
else:
    print('Sua media é {} e voce está APROVADO'.format(media))
