matriz=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0, 3):
        n=int(input(f'Digite o valor para [{x},{y}]: '))
        matriz[x][y]=n
print('='*15)
print(f'{'MATRIZ FORMADA':^15}')
print('='*15)
for x in range(0,3):
    for y in range(0,3):
        print(f'{matriz [x] [y]:^5}', end='')
    print()
print('='*15)
pares=0                         #SOMA DOS VALORES PARES
for x in range(0,3):
    for y in range(0, 3):
        s=matriz[x][y]
        if s%2==0:
            pares=pares+s
coluna3=0                       #SOMA DA COLUNA 3
for tc in range(0,3):
    coluna3+=matriz [tc][2]
for m in range(0,3):            #MAIOR VALOR DA LINHA 2
    if m==0:
        maior=matriz [1] [m]
    elif matriz [1] [m] > maior:
        maior = matriz [1] [m]
print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna3}')
print(f'O maior valor da segunda linha é: {maior}')


