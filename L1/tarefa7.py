#Todos os Imputs

nome_1 = input()
quem_indicou_1 = input()
nome_2 = input()
quem_indicou_2= input() 
nome_3 = input()
quem_indicou_3 = input()

#Pontuação Nome 1

if(quem_indicou_1=='felino espião'):
    nota1=0
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

elif(('gato'in nome_1) or ('felino' in nome_1)):
    nota1=0
else:
    nota1= len(nome_1)
    if('cin' in nome_1):
        nota1+=10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')


#Pontuação Nome 2

if(quem_indicou_2=='felino espião'):
    nota2=0
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

elif(('gato' in nome_2) or ('felino' in nome_2)):
    nota2=0
else:
    nota2= len(nome_2)
    if('cin' in nome_2):
        nota2+=10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')


#Potuação Nome 3

if(quem_indicou_3=='felino espião'):
    nota3=0
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

elif(('gato'in nome_3) or ('felino' in nome_3)):
    nota3=0
else:
    nota3= len(nome_3)
    if('cin' in nome_3):
        nota3+=10
        print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

#Ranking

if(nota1>nota2 and nota1>nota3):
    print(f'RANKING DOS NOMES:\nPrimeiro lugar: {nome_1}')
    if(nota2>nota3):
        print(f'Segundo lugar: {nome_2}\nTerceiro lugar: {nome_3}')
    else:
        print(f'Segundo lugar: {nome_3}\nTerceiro lugar: {nome_2}')
elif(nota2>nota3 and nota2>nota1):
    print(f'RANKING DOS NOMES:\nPrimeiro lugar: {nome_2}')
    if(nota1>nota3):
        print(f'Segundo lugar: {nome_1}\nTerceiro lugar: {nome_3}')
    else:
        print(f'Segundo lugar: {nome_3}\nTerceiro lugar: {nome_1}')
else:
    print(f'RANKING DOS NOMES:\nPrimeiro lugar: {nome_3}')
    if(nota2>nota1):
        print(f'Segundo lugar: {nome_2}\nTerceiro lugar: {nome_1}')
    else:
        print(f'Segundo lugar: {nome_1}\nTerceiro lugar: {nome_2}')
    



