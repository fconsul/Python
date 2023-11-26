#ler comprimento de tres retas e diga se elas foram triangulo
r1 = float(input('Digite o comprimento de uma reta '))
r2 = float(input('Digite o comprimento de uma segunda reta '))
r3 = float(input('Digite o comprimento de uma terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas três retas formam um triângulo')
else:
    print('Estas três retas NÃO formam um triângulo')