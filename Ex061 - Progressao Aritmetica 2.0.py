print('='*21)
print('10 TERMOS DE UMA P.A.')
print('='*21)
cont=0
razao=int(input('Digite a razão da P.A.: '))
primeiro=int(input('Digite o primeiro termo: '))
while cont < 10:
    print(primeiro, end=' -')
    primeiro=primeiro+razao
    cont=cont+1
print(' FIM', end='')

