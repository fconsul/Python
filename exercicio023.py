#ler numero de 0 a 9999 e mostre os digitos separados
#estou perdido
numero=int(input('Digite um número de 0 a 9999 '))
unidade=numero // 1 % 10
dezena=numero // 10 % 10
centena=numero // 100 % 10
milhar=numero // 1000 % 10
print('Unidade {}, dezena {}, centena {} e milhar {}'.format(unidade,dezena,centena,milhar))