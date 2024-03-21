n1=float(input('Informe o 1º número: '))
n2=float(input('Informe o 2º número: '))
if n1>n2:
    print('{} é o maior número.'.format(n1))
elif n1<n2:
    print('{} é o maior número.'.format(n2))
elif n1==n2:
    print('Nenhum dos dois números é maior, pois eles são iguais.')
