import random
from time import sleep
computador=random.randint(1,3)
jogada=int(input('[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nQual a sua jogada? '))
print('#### JO ####')
sleep(0.5)
print('#### KEN ####')
sleep(0.5)
print('#### PÔ ####')
sleep(0.5)
if jogada==1 or jogada==2 or jogada==3:
    if computador==1:
        if jogada==1:
            jogador='PEDRA'
            ganhador='NINGUÉM'
        if jogada==2:
            jogador = 'PAPEL'
            ganhador = 'VOCÊ'
        if jogada==3:
            jogador = 'TESOURA'
            ganhador='O COMPUTADOR'
        print('-='*14)
        print('O computador escolheu PEDRA.\nVocê escolheu {}.\n{} ganhou!'.format(jogador,ganhador))
        print('-=' * 14)
    elif computador==2:
        if jogada==1:
            jogador = 'PEDRA'
            ganhador='O COMPUTADOR'
        if jogada==2:
            jogador = 'PAPEL'
            ganhador = 'NINGUÉM'
        if jogada==3:
            jogador = 'TESOURA'
            ganhador='VOCÊ'
        print('-=' * 14)
        print('O computador escolheu PAPEL.\nVocê escolheu {}.\n{} ganhou!'.format(jogador,ganhador))
        print('-=' * 14)
    elif computador==3:
        if jogada==1:
            jogador = 'PEDRA'
            ganhador='VOCÊ'
        if jogada==2:
            jogador = 'PAPEL'
            ganhador = 'O COMPUTADOR'
        if jogada==3:
            jogador = 'TESOURA'
            ganhador='NINGUÉM'
        print('-=' * 14)
        print('O computador escolheu TESOURA.\nVocê escolheu {}.\n{} ganhou!'.format(jogador,ganhador))
        print('-=' * 14)
elif jogada==str:
    print('Opção inválida. Tente novamente.')
else:
    print('Opção inválida. Tente novamente.')



