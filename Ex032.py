from datetime import date
ano=int(input('Digite o ano para saber se ele é bissexto (digite 0 para analisar o ano atual: '))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('\033[1;34mSIM\033[m, o ano de {} é Bissexto.'.format(ano))
else:
    print('\033[1;31mNÃO\033[m, o ano de {} NÃO É Bissexto'.format(ano))
