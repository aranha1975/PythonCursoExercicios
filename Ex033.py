n1=int(input('Digite o 1º número: '))
n2=int(input('Digite o 2º número: '))
n3=int(input('digite o 3º número: '))
if n1>=n2 and n1>=n3:
    ma=n1
if n2>=n1 and n2>=n3:
    ma=n2
if n3>=n1 and n3>=n2:
    ma=n3
if n1<=n2 and n1<=n3:
    me=n1
if n2<=n1 and n2<=n3:
    me=n2
if n3<=n1 and n3<=n2:
    me=n3
print('O MAIOR número é o número {}'. format(ma))
print('O MENOR número é o número {}'.format(me))
