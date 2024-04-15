lista=[]
dados=[]
pesados=[]
leves=[]
while True:
    nome=str(input('Nome: '))
    peso=int(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    if len(lista) == 1:
        maior = menor = peso
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
    dados.clear()
    sn=str(input('Quer continuar? [S/N]: '))
    if sn in 'Nn':
        break
print(lista)
print(f'Você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi {maior} Kg, peso de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ',end='')
print(f'\nO menor peso foi de {menor} Kg, peso de ', end='')
for c in lista:
    if c[1] == menor:
        print(f'{c[0]} ', end='')



