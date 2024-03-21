import math
n=int(input('Digite um número: '))
if (n%2)==0:
    print('O número {} é {}PAR'.format(n,'\033[1;34m'))
else:
    print('O número {} é {}ÍMPAR'.format(n, '\033[1;31m'))

