lista=[]
dados=[]
while True:
    nome=str(input('Nome: '))
    dados=[]
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    lista.append(dados[:])
    parar=str(input('Deseja Continuar? [S/N]: '))
    if parar in 'Nn':
        break
print('='*23)
print(f'{"BOLETIM ELETRÔNICO":^23}')
print('='*23)
print(f'{"Nº":<5}{"NOME":<12}{"MÉDIA":>5}')
print('-'*23)
for c in range(len(lista)):
    print(f'{c+1:<5}', end='')
    print(f'{lista[c][0]:<12}',end='')
    print(f'{(lista[c][1]+lista[c][2])/2:>5}')
print('-'*60)
while True:
    aluno = int(input('Digite nº do aluno para ver as notas dele ou 999 para parar: '))
    if aluno == 999:
        break
    else:
        print(f'As notas do aluno {lista[aluno-1][0]} são {lista[aluno-1][1]} e {lista[aluno-1][2]}')
        print('-'*60)
print('Obrigado por consultar nosso BOLETIM ELETRÔNICO')