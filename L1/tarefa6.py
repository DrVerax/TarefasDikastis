#Colocando os Valores
#Byte Tá aí?

nome_cao1=input() 
pontuação_prova_11=int(input()) 
pontuação_prova_21=int(input())
pontuação_prova_31=int(input())
som1= (pontuação_prova_11 + pontuação_prova_21 + pontuação_prova_31)

if(nome_cao1== 'Byte'):
    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
elif(som1==30):
    print(f'Com uma pontuação perfeita, {nome_cao1} conquista o título de mascote do CIn!')
else:
    nome_cao2=input() 
    pontuação_prova_12=int(input())
    pontuação_prova_22=int(input()) 
    pontuação_prova_32=int(input()) 
    som2= (pontuação_prova_12 + pontuação_prova_22 + pontuação_prova_32)

    if(nome_cao2== 'Byte'):
        print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
    elif(som2==30):
        print(f'Com uma pontuação perfeita, {nome_cao2} conquista o título de mascote do CIn!')
    else:
        nome_cao3=input() 
        pontuação_prova_13=int(input()) 
        pontuação_prova_23=int(input()) 
        pontuação_prova_33=int(input())
        som3= (pontuação_prova_13 + pontuação_prova_23 + pontuação_prova_33)

        if(nome_cao3== 'Byte'):
            print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
        elif(som3==30):
            print(f'Com uma pontuação perfeita, {nome_cao3} conquista o título de mascote do CIn!')

        #Byte não está na Jogada e Nínguem É Top

        else:
            if(som1>som2 and som1>som3):
                print(f'Infelizmente {nome_cao2} está fora da disputa')
                print(f'Infelizmente {nome_cao3} está fora da disputa')
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao1}!')
            elif(som2>som1 and som2> som3):
                print(f'Infelizmente {nome_cao1} está fora da disputa')
                print(f'Infelizmente {nome_cao3} está fora da disputa')
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao2}!')
            else:
                print(f'Infelizmente {nome_cao1} está fora da disputa')
                print(f'Infelizmente {nome_cao2} está fora da disputa')
                print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao3}!')
            