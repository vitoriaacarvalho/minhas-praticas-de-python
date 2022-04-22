#lista chamada números e 2 funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda vai mostrar a soma entre todos os valoress PARES sorteados pela sorteio().
from random import randint
numeros=[]
def sorteia(lista):
    for c in range (0,5):
        n=randint(1,10)
        numeros.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'somando os valores pares de {lista}, temos como resultado {soma}')    



sorteia(numeros)
somaPar(numeros)