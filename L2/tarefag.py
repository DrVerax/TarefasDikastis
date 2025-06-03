#PrintIncial

print('🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓')
print('Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!')
print('')

#Pegando Os Valores Corretos

nvl0=int(input('Qual será o número que marcará o INÍCIO dessa tabuada fatorial?\n'))
while(nvl0<0):
    print(f'O número {nvl0} é inválido! O INÍCIO NÃO pode ser NEGATIVO.')
    nvl0=int(input())

print(f'O número {nvl0} é ótimo como número inicial!')  
print('')

nvlf=int(input('Qual será o número que marcará o FIM dessa tabuada fatorial?\n'))
while((nvlf<0) or (nvlf<nvl0)):
    print(f'O número {nvlf} é inválido! O FIM NÃO pode ser MENOR que o número inicial {nvl0}.')
    nvlf=int(input())  
print(f'O número {nvlf} é ótimo como número final!')
print('')

num_sacro=int(input('Qual será o número cujo FATORIAL será calculado?\n'))
while(num_sacro<0):
    print(f'O número {num_sacro} é inválido! Números válidos são maiores ou iguais a zero.')
    num_sacro=int(input())
print(f'O número {num_sacro} é ótimo para o cálculo do fatorial!')
print('')

#Calculo dos Fatoriais

i=nvl0
result_fat=0

while(i<=nvlf):
    k=1
    j=i*num_sacro
    while(j>=1):
        k=j*k
        j-=1
    print(f'({i} * {num_sacro})! = {k}')
    i+=1

#Print Final

print('')
print('🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!')
print('🏓 Que sua energia vital continue brilhando nas próximas batalhas!')