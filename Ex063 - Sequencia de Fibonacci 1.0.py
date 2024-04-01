termos=int(input('Digite quantos termos da sequencia Fibonacci você quer ver: '))
a=0
b=1
c=a+b
cont=3
print('{} - {} - {} - '.format(a,b,c), end='')
while cont < termos:
    #print(t1+t2, end=' - ')
    cont+=1
    a = b
    b = c
    c=a+b
    if cont < termos:
        print(c,end=' - ')
    if cont == termos:
        print(c, end='')

