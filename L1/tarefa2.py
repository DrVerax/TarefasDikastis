#Leitura Valores

nome_aluno = input()
al1=int(input())
al2=int(input())
al3=int(input())
al4=int(input())*(10/6)
al5=int(input())*(10/6)
al6=int(input())*(10/6)



#Calculando A Média

media_geral = (al1+al2+al3+al4+al5+al6)/6
print(f'A média de {nome_aluno} é {media_geral:.1f}')

#Avaliação Rendimento

if(al1 > al2 or al2 > al3 or al3 > al4 or al4 > al5 or al5 > al6):
    print('Alerta! Queda no rendimento.' )
else:
    print('Progresso constante! Parabéns pelo esforço!')

#Avaliação Realização

a=0
if(al1==0):
    a+=1
if(al2==0):
    a+=1
if(al3==0):
    a+=1
if(al4==0):
    a+=1
if(al5==0):
    a+=1
if(al6==0):
    a+=1
if(a >= 2):
    print('Alerta! Múltiplas listas não respondidas.')

#Avaliação Média

if(media_geral >= 8):
    print('Parabéns pelo excelente desempenho!Continue "au" sim.')
elif(media_geral < 8 and media_geral >=7):
    print('Parabéns pelo bom desempenho!')
else:
    print('Alerta! Desempenho abaixo do esperado.')
