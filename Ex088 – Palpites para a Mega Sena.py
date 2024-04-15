from random import randint
from time import sleep
jogo=[]
print('='*40)
print(f'{'ELABORADOR DE JOGOS DAS MEGASENA':^40}')
print('='*40)
for x in range(1,(int(input('Quantos jogos deseja que eu faça? ')))+1):
    print(f'Jogo {x}: ',end='')
    for c in range(0,6):
        n=randint(1,60)
        if c not in jogo:
            jogo.append(n)
        else:
            n = randint(1, 60)
            jogo.append(n)
    jogo.sort()
    print(jogo)
    jogo.clear()
    sleep(1)
