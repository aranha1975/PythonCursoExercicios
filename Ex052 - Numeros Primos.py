n=int(input('Digite um número para verificar se é um NÚMERO PRIMO: '))
d=0
cont=0
for c in range(1,n+1):
        if n % c == 0:
            d=d+c #Acumulador s
            cont=cont+1
            l=c
if cont == 2:
    print('O número {} É UM NÚMERO PRIMO, pois 2 divisores: 1 e ele mesmo.'.format(n))
else:
    print('O número {} NÃO É UM NÚMERO PRIMO, pois tem {} divisores '.format(n, cont))






