lista=[]
pares=[]
impares=[]
while True:
    n=int(input('Digite um número: '))
    lista.append(n)
    p = input('Deseja continuar? [S/N]: ')
    if p in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Você digitou os números: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')


