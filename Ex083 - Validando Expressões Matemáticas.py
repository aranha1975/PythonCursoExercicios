#minha solução
'''e=str(input('Digite uma expressão matemática: '))
if e.count('(')==e.count(')'):
    print('A expressão matemática digitada é VÁLIDA.')
else:
    print('A expressão é INVÁLIDA')'''

#solução de Guanabara
expr=str(input('Digite uma expressao: '))
pilha=[]
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Expressão está VÁLIDA.')
else:
    print('Sua expressão é INVÁLIDA.')

