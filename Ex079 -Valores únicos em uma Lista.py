valores=[]
while True:
    n=int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado! Não foi adicionado.')
    resposta=str(input('Deseja continuar? [S] ou [N]: '))
    if resposta in 'Nn':
        break
    elif resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S] ou [N]: '))
print(sorted(valores))


