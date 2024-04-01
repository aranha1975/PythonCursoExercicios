n=cont=s=0
flag=999
n = int(input('Digite um número: '))
while n != flag:
    cont+=1
    s=n+s
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma deles é {}.'.format(cont,s))


