#programa que leia o nome dos quatro alunos e mostra a ordem sorteada
import random
aluno1='Kiko'
aluno2='Zinho'
aluno3='Lindo'
aluno4='Branco'
classe=[aluno1, aluno2, aluno3, aluno4]
random.shuffle(classe)
print('A ordem de apresentação será {}'.format(classe))