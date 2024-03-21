num=int(input('Digite um número de 0000 a 9999: '))
uni= num//1 %10
dez= num//10 %10
cen=num//100 %10
mil=num//1000 %10
print('Analisando o número {}...'.format(num))
print('A unidade deste número é {}.'.format(uni))
print('A dezena deste número é {}.'.format(dez))
print('A centena desde número é {}.'.format(cen))
print('O milhar desse número é {}.'.format(mil))

