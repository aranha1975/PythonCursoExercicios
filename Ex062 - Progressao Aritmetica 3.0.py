print('='*21)
print('10 TERMOS DE UMA P.A.')
print('='*21)
cont=0
razao=int(input('Digite a razão da P.A.: '))
primeiro=int(input('Digite o primeiro termo: '))
while cont < 10:
    print(primeiro, end='-')
    primeiro=primeiro+razao
    cont w w=cont+1
print('PAUSA')
mais=1
while mais != 0:
    mais=int(input('Quer mostrar mais termos? Quantos? '))
    contmais=cont+mais
    while cont < contmais:
        print(primeiro, end='-')
        primeiro = primeiro + razao
        cont = cont + 1
    if mais == 0:
        print('FIM', end='')
        print('')
    else:print('PAUSA', end='')
    print('')
print('Progressão finalizada com {} termos mostrados.'.format(cont))


