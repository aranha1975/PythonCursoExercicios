matriz=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0, 3):
        n=int(input(f'Digite o valor para [{x},{y}]'))
        matriz[x][y]=n
for x in range(0,3):
    for y in range(0,3):
        print(f'{matriz [x] [y]:^5}', end='')
    print()

