
fome = input('O Byte está com fome?\n')
if (fome == 'sim'):
    escolha = input('O que você vai dar para ele comer?\n')
    if(escolha == 'carne' or escolha== 'petisco' or escolha== 'ração'):
        print(f'Byte comeu {escolha} e está feliz!')
        print('Depois desse banquete, Byte pode tirar um cochilo feliz')
    else:
        print(f'Byte não gosta de {escolha}\n')
        print(f'Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas...')
elif(fome == 'não'):
    print('Já que Byte não está com fome, ele pode passear')
    passeio_ok = input('Está chovendo?\n')
    if (passeio_ok=='sim'):
        print('Já que está chovendo, Byte vai ter que brincar em casa')
    elif(passeio_ok=='não'):
        print('Byte está indo passear')
    else:
        print('Insira um resposta válida')
else:
    print('Insira uma resposta válida')       
