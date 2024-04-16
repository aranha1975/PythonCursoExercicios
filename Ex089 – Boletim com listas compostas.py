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
print(dados)
print(lista)
#tô tentando descobrir como ele numerou cada nome no boletim