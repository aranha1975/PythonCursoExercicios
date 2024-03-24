from time import sleep
print('-=-'*10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*10)
r1=float(input('Digite o tamanho da 1ª reta: '))
r2=float(input('Digite o tamanho da 2ª reta: '))
r3=float(input('Digite o tamanho da 3ª reta: '))
print('ANALISANDO...')
sleep(3)
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('\033[1;34mTrês retas com tamanhos {}, {} e {} podem SIM formar um triângulo.'.format(r1,r2,r3))
else:
    print('\033[1;31mAs três retas com tamanhos {}, {} e {} NÃO PODEM formar um triângulo.'.format(r1,r2,r3))
