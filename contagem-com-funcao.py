from time import sleep


def contador(i,f,p):
    if p<0:
        p*=-1 
    if p==0:
        p=1
    print('=-'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i<f: #contagem crescente
        cont=i
        while cont<=f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont+=p
        print('FIM!')
    else: #para quando a contagem for decrescente
        cont=i
        while cont>=f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont-=p
        print('FIM!')


#programa principal
contador(1,10,1)
contador(10,0,2)
print('agora é sua vez de determinar os valores!')
ini=int(input('início: '))
fim=int(input('fim: '))
pas=int(input('passo: '))
contador(ini,fim,pas)