s=0
cont=0
for c in range(1,501,2):
    if c % 3 == 0:
        s=s+c #Acumulador s
        cont=cont+1 #Contador cont
print('A soma dos {} valores solicitados é {}.'.format(cont,s))
