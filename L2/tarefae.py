quantidade_atletas=int(input())
num_rodada=1
numdevog=0
player1='x'
sus1=0
player2='x'
sus2=0
player3='z'
sus3=0

#Me Livrando Dos Casos Especiais

if(quantidade_atletas==1):
    atleta=input()
    print(f'Não há dúvidas... {atleta} é o culpado!')
elif(quantidade_atletas==2):
    atleta_1=input()
    posicao=int(input())
    ranking=int(input())
    vel=float(input())
    atleta_2=input()
    posicao2=int(input())
    ranking2=int(input())
    vel2=float(input())
    print(f'Caso encerrado: {atleta_1} e {atleta_2} roubaram o troféu!')

#Casos Normais Lelek

else:

    while(num_rodada<=quantidade_atletas):
        numdevog=0
        sus=0
        atleta=input()
        posicao=int(input())
        ranking=int(input())
        vel=float(input())

        print(f'COMEÇANDO A {num_rodada}ª RODADA DE INVESTIGAÇÃO')

        #Codição de Frases
        if((posicao>=45) and (posicao<=135)):
            print(f'{atleta} estava em posição estratégica para pegar o troféu... muito suspeito!')
        if(ranking<=10):
            print(f'{atleta} é um dos melhores do mundo... e também um dos principais suspeitos!')
        if(vel>=140):
            print(f'Alta velocidade detectada! {atleta} pode ter fugido rapidamente com o troféu!')
        if((posicao<45 or posicao>135) and (ranking>10) and (vel<140) ): 
            print(f'Hum, esse {atleta} sei não viu... Deve tá escondendo alguma coisa.')

        #Condição de Pontuação
        if((posicao>=45) and (posicao<=135)):
            sus+=10
        elif((posicao>=225) and (posicao<=315)):
            sus+=5
        else:
            sus+=2
        
        if(ranking<=10):
            sus+=10
        elif((ranking<=50) and (ranking>=11)):
            sus+=5
        else:
            sus+=2

        if(vel>140):
            sus+=10
        elif((vel<=140) and (vel>=100)):
            sus+=5
        else:
            sus+=2
        
        for i in atleta:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                numdevog+=1
        if((numdevog%2)==0):
            sus+=10
        else:
            sus+=5
        
        num_rodada+=1

        
    #Montando o ranking

        if((sus>sus1)):

            player3=player2
            player2=player1
            sus3=sus2
            sus2=sus1
            sus1=sus
            player1=atleta

        elif((sus>sus2)):

            player3=player2
            sus3=sus2
            sus2=sus
            player2=atleta

        elif((sus>sus3)):
            sus3=sus
            player3=atleta


    #Printando

    print('')
    print('RESULTADOS DAS INVESTIGAÇÕES:')
    print('')
    print('Os 3 principais suspeitos são:')        
    print(f'1. {player1} - {sus1} pontos')
    print(f'2. {player2} - {sus2} pontos')
    print(f'3. {player3} - {sus3} pontos')
    print('')
    if(sus1==sus2):
        print(f'Que absurdo... {player1} e {player2} roubaram o troféu juntos!')
    else:
        print(f'Mistério resolvido: O culpado é {player1}! Ele roubou o troféu de Calderano.')