from random import randint
print('-='*5,'JOGO DO PAR OU ÍMPAR','=-'*5)
cont=0
pi=''
while True:
    jogador=int(input('Diga um número: '))
    while pi.upper() != 'P' and pi.upper() != 'I':
        pi=str(input('Par ou Impar? [P] ou [I]: '))
    computador=randint(1,11)
    soma=jogador+computador
    if soma %2 == 0 :
        resultado = 'PAR'
        respi='P'
    else:
        resultado = 'ÍMPAR'
        respi='I'
    print('-'*52)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, DEU {resultado}')
    print('-' * 52)
    if pi.upper() == respi:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-'*8)
    else:
        print('Você PERDEU!')
        print('-=-' * 8)
        break
    cont += 1
print(f'GAME OVER! Você consiguiu {cont} vitórias seguidas.')


