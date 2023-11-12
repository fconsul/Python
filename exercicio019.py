import random
aluno1='Kiko'
aluno2='Zinho'
aluno3='Lindo'
aluno4='Branco'
sorteado=random.choice([aluno1, aluno2, aluno3, aluno4])
print('Queridos alunos {}, {}, {} e {}, vou sortear um de vocês para apagar o quadro. O sorteado é {}'.format(aluno1, aluno2, aluno3, aluno4, sorteado))