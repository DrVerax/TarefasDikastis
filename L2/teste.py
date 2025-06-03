

atleta=input()
posicao=int(input())
ranking=int(input())
vel=float(input())
print(f'COMEÇANDO A {1}ª RODADA DE INVESTIGAÇÃO')

if((posicao>=45) and (posicao<=135)):
    print(f'{atleta} estava em posição estratégica para pegar o troféu... muito suspeito!')
if(ranking<=10):
    print(f'{atleta} é um dos melhores do mundo... e também um dos principais suspeitos!')
if(vel>=140):
    print(f'Alta velocidade detectada! {atleta} pode ter fugido rapidamente com o troféu!')
else: 
    print(f'Hum, esse {atleta} sei não viu... Deve tá escondendo alguma coisa.')