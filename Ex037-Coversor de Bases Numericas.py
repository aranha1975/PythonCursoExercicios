decimal=int(input('Escolha um número inteiro: '))
binario=bin(decimal)
octal=oct(decimal)
hexadecimal=hex(decimal)
opcao=int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\nSua opção: '))
if opcao==1:
    print('O número {} em Binário é {}.'.format(decimal,binario))
elif opcao==2:
    print('O número {} em Octal é {}.'.format(decimal, octal))
elif opcao==3:
    print('O número {} em Hexadecimal é {}'.format(decimal,hexadecimal))
else:
    print('O opção digitada é inválida.')

#Fim do código#

