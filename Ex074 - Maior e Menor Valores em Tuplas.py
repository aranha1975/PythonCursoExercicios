from random import randint
num=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = menor = num[0]
for c in (num):
    if c > maior:
        maior=c
    if c < menor:
        menor=c
print ('Os números sorteados foram: ')
for n in num:
    print(n, end=' ')
print('\nO maior número sorteado foi o número {}'. format(maior))
print(f'O menor número sorteado foi o número {menor}')

