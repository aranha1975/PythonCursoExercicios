from random import shuffle
a1=input('Nome do Primeiro Aluno: ')
a2=input('Nome do Segundo Aluno: ')
a3=input('Nome do Terceiro Aluno: ')
a4=input('Nome do Quarto Aluno: ')
lista=[a1,a2,a3,a4]
shuffle(lista)
print('A sequência de apresentação dos trabalhos do primeiro para o último será a seguinte: ')
print(lista)
