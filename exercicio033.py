#ler 3 numeros e falar qual o maior e menor
n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
n3 = int(input('Digite mais um número '))
maximo = max(n1,n2,n3)
minimo = min(n1,n2,n3)
print('O maior número digitado é {} e o menor é {}'.format(maximo, minimo))