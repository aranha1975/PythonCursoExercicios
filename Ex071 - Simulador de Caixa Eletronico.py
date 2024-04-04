#saque=int(input('Quanto deseja sacar? '))
#nota100=(saque//100)
#saque=saque%100
#nota50=saque//50
#saque=saque%50
#nota20=saque//20
#saque=saque%20
#nota10=saque//10
#saque=saque%10
#nota5=saque//5
#saque=saque%5
#nota1=saque//1
#saque=saque%1
#print('Serão entregues:\n{} notas de R$100\n{} notas de R$50\n{} notas de R$20\n{} notas de R$10\n{} notas de R$5\n{} notas de R$1'.format(nota100,nota50,nota20,nota10,nota5,nota1))
print('='*31)
print('{:^31}'.format('BANCO ARANHA'))
print('='*31)
saque=int(input("Quanto você deseja sacar? "))
cedulas=(100,50,20,10,5,1)
print('-'*31)
for c in cedulas:
    nota=saque//c
    saque=saque%c
    if nota>0:
        print('Total de {} cédulas de R${}.'.format(nota,c))
print('='*31)
print('{:^31}'.format('OBRIGADO E VOLTE SEMPRE!'))
print('='*31)