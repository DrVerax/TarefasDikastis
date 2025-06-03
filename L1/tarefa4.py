#Recebendo o Valor

dol_rec= int(input())
val_dol=float(input())
gasto_ração= int(input()) 
gasto_aluguel= int(input())   
gasto_busao= int(input())   

#Superávit?

a=dol_rec*val_dol
b=gasto_ração + gasto_aluguel + gasto_busao
c= a - b

#Análise Booleana

if(c>0):
    print('Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!')
elif(c==0):
    print('Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!')
else:
    print('Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!')

#Segunda Análise Booleana

if(gasto_aluguel>gasto_busao and gasto_aluguel> gasto_ração)    :
    print('Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!')
elif(gasto_busao>gasto_aluguel and gasto_busao>gasto_ração):
    print('Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!')
else:
    print('A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!')

#Mais Uma Análise Booleana Pq Eu Tentei Ser Malandro E Não Deu Certo

if(gasto_aluguel>gasto_busao and gasto_aluguel> gasto_ração)    :
    d='Aluguel'
elif(gasto_busao>gasto_aluguel and gasto_busao>gasto_ração):
    d= 'Ônibus'
else:
    d='Ração'


#Fim
print(f'MESADA (dólares): {dol_rec:.2f} dólares')
print(f'MESADA (reais): {a:.2f} reais')
print(f'MAIOR GASTO: {d}')