#Definições Iniciais

pntsJ=0
pntsL=0

#Primeiros Inputs

numero_rodadas=int(input())
vencedor_tomada=input()

#Primeiro Print

print('Vamos dar início à disputa!!! TOMADA!!!')

if(vencedor_tomada=='Jaob'):
    print('Jaob veio de Catende e está pronto para vencer!!!')
    manodavez='Jaob'
else:
    print('Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!')
    manodavez='Luvusier'

#Looping Variáveis

i=1
pegou_no_baralho=False

#Looping Namoral

while(i<=numero_rodadas):
    jogouniond='x'
    errado=False
    acertou=False
    print(f'COMEÇA A {i}ª RODADA!')
    i+=1

    while(acertou!=True):

        jogouniond=input()
        
        if((jogouniond=='mesa')):   
            print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
            
        elif(jogouniond=='Baralho de UNO'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ+=2
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL+=2
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsL} pontos.')
        elif(jogouniond=='Armário de Homero e Elena'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ+=3
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL+=3
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsL} pontos.')
        elif(jogouniond=='Peça de Dominó'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ+=3
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL+=3
                acertou=True
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsL} pontos.')

        elif(jogouniond=='Baralho de Coup Desaparecido'):
            if(manodavez=='Jaob'):
                pntsJ+=100
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsJ} pontos.')
                print(f'{manodavez} achou o Coup!!! Ele merece a vitória sem dúvidas!')
                acertou=True
                pegou_no_baralho=True
            else:
                pntsL+=100
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                print(f'{manodavez} teve uma grande pontaria e acertou {jogouniond}! Agora está com {pntsL} pontos.')
                print(f'{manodavez} achou o Coup!!! Ele merece a vitória sem dúvidas!')
                acertou=True
                pegou_no_baralho=True
        
        elif(jogouniond=='Projetor'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ-=2
                if(pntsJ<0):
                    pntsJ=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL-=2
                if(pntsL<0):
                    pntsL=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsL} pontos.')

        elif(jogouniond=='Computador'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ-=3
                if(pntsJ<0):
                    pntsJ=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')   
                pntsL-=3
                if(pntsL<0):
                    pntsL=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsL} pontos.')

        elif(jogouniond=='Cabeça do Amiguinho'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ-=5
                if(pntsJ<0):
                    pntsJ=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL-=5
                if(pntsL<0):
                    pntsL=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsL} pontos.')

        elif(jogouniond=='Nada'):
            if(manodavez=='Jaob'):
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsJ-=1
                if(pntsJ<0):
                    pntsJ=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsJ} pontos.')
            else:
                print(f'{manodavez} jogou a bolinha no(a) {jogouniond}!')
                pntsL-=1
                if(pntsL<0):
                    pntsL=0
                acertou=True
                errado=True
                print(f'{manodavez} teve mãos de alface e acertou o(a) {jogouniond}. Agora está com {pntsL} pontos.')

        if(pegou_no_baralho==True):
            i=numero_rodadas+1
        if(acertou==True):
            if(errado==True):
                if(manodavez=='Jaob'):
                    manodavez='Luvusier'
                else:
                    manodavez='Jaob'
        else:    
            if(manodavez=='Jaob'):
                manodavez='Luvusier'
            else:
                manodavez='Jaob'

    

#Print Final

print('\nTEMOS O RESULTADO DA PARTIDA!')

if(pntsJ==pntsL):
    print('Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!')
elif(pntsL>pntsJ):
    print(f'A química está em festa, Luvusier ganha a disputa com {pntsL} pontos!')
else:
    print(f'Jaob deu orgulho à Catende e ganhou a disputa com {pntsJ} pontos!')
