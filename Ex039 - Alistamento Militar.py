from datetime import date
anoatual=date.today().year
ano=int(input('Digite o ano que você nasceu: '))
idade=anoatual-ano
if idade == 17:
    print('Você tem {} anos, então ainda falta 1 ano para seu alistamento militar. Seu alistamente será em {}.20010'.format(idade, (ano+18)))
elif idade < 17:
    print('Você tem {} anos, então ainda faltam {} anos para seu alistamento militar. Seu alistamente será em {}.'.format(idade,(18-idade), (ano+18)))
elif idade==18:
    print('Você tem {} anos, terá que fazer o alistamento militar ESTE ANO.'.format(idade))
elif idade==19:
    print('Você tem {} anos. Era pra você ter feito alistamento militar há 1 ano, no ano de {}. '.format(idade,(ano+18)))
else:
    print('Você tem {} anos. Era pra você ter feito alistamento militar há {} anos, no ano de {}. '.format(idade,(idade-18),(ano+18)))

