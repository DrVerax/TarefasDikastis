#PréDefinições

nacionalidade_atleta='OI'
print('A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!')
numero_adversário=0
numero_hugo=0
auxadv=0
auxhugo=0

#PegandoONome

while(nacionalidade_atleta!='Chinês'):
    nacionalidade_atleta=input()
    nome_atleta=input()
    if(nacionalidade_atleta!='Chinês'):
        print(f'O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!')

print(f'{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!')

#Partida

while ((abs(auxadv-auxhugo))<3):
    numero_adversário=int(input())
    numero_hugo=int(input())
    if((numero_adversário>=(2*numero_hugo))):
        auxadv+=2
        print('Que bela jogada, essa merece ponto extra!')
    elif((numero_adversário>numero_hugo) and (numero_adversário<(2*numero_hugo))):
        auxadv+=1
        print('Vamos Hugo, não deixe ele vencer!')
    if((numero_hugo>=(2*numero_adversário))):
        auxhugo+=2
        print('Que bela jogada, essa merece ponto extra!')
    elif((numero_hugo>numero_adversário) and (numero_adversário<(2*numero_hugo))):
        auxhugo+=1 
        print('Hugo Calderano marcou um ponto de maneira esplendida!') 
    if(numero_adversário==numero_hugo):
        auxhugo+=1
        print('A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!')

#Comentários Da Partida

if(auxhugo==3):
    print('Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!')
elif((auxhugo>3) and (auxhugo<=10)):
    print('Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!')
elif(auxhugo>10):
    print('Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!')

#Placar e Prêmio

print(f'Placar Final: {auxhugo}x{auxadv}\n')
print('Aqui está o merecido prêmio de Hugo Calderano:')

#Evitando Problemas No Troféu

if(((auxadv%2)==0) and (auxadv>2)):
    auxadv-=1
elif(auxadv<=2):
    auxadv=3

#Printando Troféu

numaux1=1

while(numaux1<=auxadv):

    i=1
    j=1
    k=1
    
    if((numaux1==1) or (numaux1==auxadv)):
        while(i<=auxhugo):
            print('-', end='')
            if(i==auxhugo):
                print('')
            i+=1

    elif((numaux1!=1) and (((auxadv//2) + 1)!=numaux1) and (numaux1!=auxadv)):
        while(j<=auxhugo):
            if((j==1) or (j==auxhugo)):
                print('|', end='')
            else:
                print(' ', end='')
            if(j==auxhugo):
                print('')
            j+=1

    elif(((auxadv//2) + 1)==numaux1):
        while(k<=auxhugo):
            if((k==1 )or (k==auxhugo)):
                print('|',end='')
            else:
                print('#', end='')
            if(k==auxhugo):
                print('')
            k+=1
            
    numaux1+=1





