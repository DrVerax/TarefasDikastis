#primeiros inputs

F_max=int(input())
força_inicial=int(input())
nivel=input()
força_media_jogador=int(input())

#PrélOOp

F_rebatida=força_inicial
F_acumulada=0
Força_media_robo=0
print('Robô Hugo 4.0 foi inicializado…')
n=1
força_total=0

#CondicionaisPréLoop

if(nivel=='facil'):
    print('Iniciando no modo iniciante... Ótimo para aquecer os motores!')
    i=1
elif(nivel=='medio'):
    print('Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!')
    i=3
else:
    print('Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!')
    i=5

#Loop

while((força_total<F_max) and (F_rebatida<150)):

    F_rebatida=força_inicial+(n*i)
    força_total=F_rebatida+força_total
    print(f'Rebatida {n}: força = {F_rebatida}, força acumulada = {força_total}')
    n+=1
n=n-1
#Fora do Loop
if(força_total>=F_max):
    print('Energia do robô esgotada! Encerrando o confronto…')
elif(F_rebatida>=150):
    print('Bola fora! A força da rebatida excedeu os limites da mesa.')

if(n!=0):
    bps=força_total//n
else:
    bps=0
print('Partida finalizada! Estas são as estatísticas do embate:')
print(f'O robô realizou {n} rebatidas em {n} segundos, com força total de {força_total}.')
print(f'Força média do robô: {bps}')
print(f'Força média do jogador: {força_media_jogador}')

#condicional de vitoria

if(bps>força_media_jogador):
    print('Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!')
elif(bps==força_media_jogador):
    print('Empate técnico! Um duelo digno de mestres do tênis de mesa.')
else:
    print('Vitória do jogador! O talento humano ainda é imbatível!')