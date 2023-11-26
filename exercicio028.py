#pensar um numero inteiro entre 0 e 5 e peça pro usuário tentar descobrir

import random
x = random.randint(0,5)
print('Pensei num número de 0 a 5!')
numero = int(input('Digite o número que eu estou pensando: '))
if x==numero:
    print('Mãe Dinah vive! Você acertou!')
else:
    print('Seus dons de adivinhação falharam. Você errou. Eu estava pensando no número {}'.format(x))

