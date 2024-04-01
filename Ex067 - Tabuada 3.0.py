n=0
c=1
s=0
while True:
    print('='*34)
    n = int(input('Quer ver a tabuada de que número? '))
    if n<0:
        break
    for c in range(1,10):
        print(f'{n} x {c} = {n * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre.')







