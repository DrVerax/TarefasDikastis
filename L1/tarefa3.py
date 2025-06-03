#Recebendo Valores

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

#Nova variável com a soma

som = a+b+c+d+e

#Começando a Roda  

quem_ganhou = som%5

if(quem_ganhou==0):
    print('Arthur vai ter a honra de passear com Byte hoje!')

elif(quem_ganhou==1):
    print('Bruna vai ter a honra de passear com Byte hoje!')

elif(quem_ganhou==2):
    print('César vai ter a honra de passear com Byte hoje!')

elif(quem_ganhou==3):
    print('Daniel vai ter a honra de passear com Byte hoje!')

elif(quem_ganhou==4):
    print('Eduarda vai ter a honra de passear com Byte hoje!')