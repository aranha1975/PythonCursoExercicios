contpal=0
from random import randint
numero=randint(0,10)
print('Sou seu computador.\nAcabei de pensar em um número de 0 a 10.')
print('Será que você consegue advinhar qual foi?')
palpite=int(input('Digite seu palpite: '))
while numero != palpite:
    contpal=contpal+1
    if palpite > numero:
        palpite=int(input('Menos do que isso...\nDigite um novo palpite: '))
    elif palpite < numero:
        palpite = int(input('Mais do que isso...\nDigite um novo palpite: '))
print('PARABÉNS! Eu realmente pensei no número {}.'.format(palpite))
print('Você acertou na {}ª tentativa.'.format(contpal+1))
