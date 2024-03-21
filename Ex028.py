from random import randint
from time import sleep
n=randint(1,5)
print('-=-'*20)
print('Estou pensando em um número de 1 a 5. Tente adivinhar...')
print('-=-'*20)
p=int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if p==n:
    print('\033[1;34mPARABÉNS !!! VOCÊ ADIVINHOU !!')
else:
    print('\033[1;31mVocê errou, eu pensei no número {}. Tente novamente.'.format(n))
