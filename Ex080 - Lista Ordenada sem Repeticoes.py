#minha solução
'''lista=[]
n0=int(input('Digite um número: '))
lista.append(n0)
print('Número adicionado no final da lista.')
while True:
    n=int(input('Digite um número: '))
    if n not in lista:
        for x in range(1,6):
            if n not in lista:
                if (n-x) in lista:
                    p=lista.index(n-x)
                    lista.insert((p+1),n)
                    print(f'Número {n} adicionado na posição {p+1}')
                elif (n+x) in lista:
                    p=lista.index(n+x)
                    if p==0:
                        lista.insert(0,n)
                        print(f'Número {n} adicionado na posição {0}')
                    else:
                        lista.insert((p) , n)
                        print(f'Número {n} adicionado na posição {p}')
        c=input('Deseja Continuar? [S/N]: ')
        if c not in 'SsNn':
            c=input('Deseja Continuar? [S/N]: ')
        elif c in 'Nn':
            break
    else:
        print('Valor não adicionado, pois já existe na lista')
print(lista)'''

#solução de gustavo guanabara
lista=[]
for c in range(0,5):
    n=int(input('Digite um número: '))
    if c==0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Número edicionado na posição {pos}')
                break
            pos = pos +1
print(lista)


