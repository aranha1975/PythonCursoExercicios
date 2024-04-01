opcao=1
v1 = int(input('Digite o 1º número inteiro: '))
v2 = int(input('Digite o 2º número inteiro: '))
while opcao != 5:
    print('-'*30)
    opcao = int(input('[1] - Somar\n[2] - Multiplicar\n[3} - Saber o Maior\n[4} - Informar Novos números\n[5] - Sair do Programa\nEscolha uma opção:'))
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(v1,v2,v1+v2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(v1,v2,v1*v2))
    elif opcao == 3:
        if v1>v2:
            print('O maior valor entre {} e {} é {}'.format(v1,v2,v1))
        elif v1<v2:
            print('O maior valor entre {} e {} é {}'.format(v1,v2,v2))
        else:
            print('Nenhum dos dois é maior, pois ambas tem o mesmo valor.')
    elif opcao == 4:
        print('-' * 30)
        v1 = int(input('Digite o 1º número inteiro: '))
        v2 = int(input('Digite o 2º número inteiro: '))
        #opcao=int(input('[1] - Somar\n[2] - Multiplicar\n[3} - Saber o Maior\n[4} - Informar Novos números\n[5] - Sair do Programa\nEscolha uma opção:'))
    elif opcao > 5:
        print('Opção inválida.')
print('-' * 30)
print('Obrigado por utilizar nosso sistema')
print('-' * 30)



