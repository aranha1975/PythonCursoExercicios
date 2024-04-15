lista=[]
cont=0
while True:
    n=int(input('Digite um número: '))
    lista.append(n)
    p = input('Deseja continuar? [S/N]: ')
    if p in 'Nn':
        break
print(f'Você digitou {len(lista)} números.')
a=lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 está na {lista.index(5)+1}ª posição da lista.')
else:
    print('O valor 5 não está na lista.')
