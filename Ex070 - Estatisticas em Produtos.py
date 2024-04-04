print('-'*20)
print('LOJAS SUPER BARATÃO')
print('-'*20)
continuar=''
tot=cont1000=0
cont=0
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço: '))
    tot=tot+preco
    cont+=1
    if preco > 1000:
        cont1000=cont1000+1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        produtobarato=produto

    continuar = str(input('Quer continuar? [S ou N]: '))
    while continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar = str(input('Quer continuar? [S ou N]: '))
    if continuar.upper() == 'N' :
            break
print('-'*10,'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi R$ {tot:.2f}.')
print(f'Temos {cont1000} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {produtobarato}, que custou R$ {maisbarato:.2f}.')
