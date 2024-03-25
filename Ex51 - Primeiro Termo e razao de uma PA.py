print('='*31)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*31)
pt = int(input('Primeiro Termo da P.A: '))
razao = int(input('Razão da P.A.:'))
cont=0
for c in range(pt,1000,razao):
    c=c+razao
    cont=cont+1
    if cont >10:
        break
    print((c - razao),end=' ')

#x=pt+razao
#for c in range(pt,x,razao)