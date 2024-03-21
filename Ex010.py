r=float(input('Quantos Reais você tem na carteira?'))
cotação=4.92
d=r//cotação
re=r%cotação
print('Com R${:.2f} você pode comprar U${:.2f} e ainda sobram R${:.2f}.'.format(r,d,re))

