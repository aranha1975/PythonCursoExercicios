galera=[]
dados=[]
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if 80>p[1]>60:
        print(f'{p[0]} é preferencial, pois tem mais de 60 anos.')
    elif p[1]>80:
        print(f'{p[0]} é preferencial especial, pois tem mais de 80 anos.')
    else:
        print(f'{p[0]} não é preferencial , pois tem menos de 60 anos.')
print(galera)