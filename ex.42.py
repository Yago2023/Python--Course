print('-' * 20)
print('\33[31mTeste de Triangulo\33[m')
print('-'* 20)
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outyro  número: '))
if a < b + c and b < c + a and c < a + b:
    print('Os seguimentos formam um triangulo')
    if a == b ==c:
        print('\33[31mTriangulo é equilatero\33[m')
    elif a != b != c != a:
        print ('\33[31mTriagulo é escaleno\33[m')
    else:
        print('\33[31mTriangulo é isosceles\33[m')
else:
    print(' Os seguimentos \33[31mNÃO\33[m formam um triangulo')
