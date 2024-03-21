s=float(input('Qual o valor exato de seu salário? '))
if s>= 1250:
    a=0.1
    print('Seu aumento será de {}% e seu novo salário será R${:.2f}.'.format((a*100),(s*(1+a))))
else:
    a=0.15
    print('Seu aumento será de {}% e seu novo salário será R${:.2f}.'.format((a*100),(s*(1+a))))

