#leia frase e mostre quantos A, em que posição aparece pela primeira vez, em que posição aparece por ultimo

frase=input('Digite uma frase ')
print('A frase digitada tem {} letras A'.format(frase.lower().count('a')))
print('A primeira letra A está na posição {}'.format(frase.lower().find('a')))
print('A última letra A está na posição {}'.format(frase.lower().rfind('a')))