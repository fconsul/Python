#programa que leia nome completo de uma pessoa e mostre
#nome com todas letras maiusculas, minusculas, quantas letras sem contar espaços, quantas letras primeiro nome

nome=input('Digite seu nome completo ')
maiusculas=nome.upper()
minusculas=nome.lower()
print(nome)
print('Nome só com maiúsculas: {}'.format(maiusculas)) #nao dá pra fazer o nome.upper dentro?
print('Nome só com minúsculas: {}'.format(minusculas))
nomedividido=nome.split()
print('Quantidade de letras desconsiderando espaços: {}'.format(len(nome.replace(' ',''))))
print('Total de letras do primeiro nome: {}'.format(len(nomedividido[0]))) #nao dá pra fazer dentro?