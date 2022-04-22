#n1=float(input('digite a primeira nota:'))
#n2=float(input('digite a segunda nota:'))
#media=(n1+n2)/2
#if media>7:
    #print(f'sua média foi {media} e você foi aprovado!')
#else:
  #  print(f'sua média foi {media} e você foi reprovado!')
#cont=1
#anoatual=2022
#menor=0
#maior=0
#for c in range(1,7):
    #ano=int(input(f'Em que ano a {cont}° pessoa nasceu?'))
    #cont+=1
    #if (anoatual-ano)>18:
        #maior+=1
    #else:
        #menor+=1
#print(f'ao todo tivemos {cont} pessoas')
#print(f'Ao todo tivemos {maior} pessoas maiores de idade')
#print(f'E também tivemos {menor} pessoas menores de idade')
#hOuM=""
#sexo=str(input('Digite seu sexo: [M/F]')).strip().upper()
#while sexo[0] not in 'FM':
    #sexo=str(input('Tente novamente. Digite seu sexo: [M/F]')).#strip().upper()
#if sexo=="M":
    #hOuM="Um homem"
#else:
    #hOuM="Uma mulher"

#print(f'legal! então quer dizer que você é {hOuM}')
#tot18=toth=totm20=0
#while True:
    #idade=int(input('Idade:'))
    #sexo=' '
    #while sexo not in 'MF':
        #SEXO=str(input('Sexo: [M/F]')).strip().upper()[0]
    #if idade>=18:
        #tot18+=1
    #if sexo =='M':
        #toth+=1
    #if sexo=='F' and idade<20:
        #totM20+=1
    #resp= ''
    #while resp not in 'SN':
        #resp= str(input('Quer continuar? [S/N]')).strip().upper()[0]
        #if resp=='N':
            #break
#print(f'total de pessoas com mais de 18 anos: {tot18}')
#print(f'ao todo temos {toth} homens cadastrados')
#print(f'e temos {totm20} mulheres com menos de 20 anos')
#numeros=('zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze','doze','treze','quatorze','quinze')
#n=int(input('Digite um número de 0 a 15:'))
#if 0<=n<=15:#
    #print(numeros[n])
#else:
    #n=int(input('Tente novamente. Digite um número de 0 a 15:'))
#numeros=('zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze','doze','treze','quatorze','quinze')
#while True:
    #n=int(input('Digite um número de 0 a 15:'))
    #if 0<=n<=15:
        #break
    #else:
        #print('tente novamente.')
#print(f'você digitou o número {numeros[n]}')

from operator import length_hint


#vinteprimeiros=('rosinha', 'cruzeiro', 'limão','torta', 'bacia','timao','jiboia','recife', 'miramar','anna','vitoria','cowboylikeme','ingles','exemplo','guanabara','academia','cafecomleite' 'santa cruz','ferdfdp','dark','taytay')

#print(f'os cinco primeiros colocados são {vinteprimeiros[0:5]}')
#print(f'os quatro últimos colocados são {vinteprimeiros[-4:]}')
#print(f'os times em ordem albética são: {sorted(vinteprimeiros)}')
#print(f'o cowboylikeme está na {vinteprimeiros.index("cowboylikeme")}° posição'#)
 # from random import randint
#numeros=(randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10#),)
#print('s valor sorteados foram:')
#for n in numeros:
 # print(f'{n} ', end='')
#print(f'O maior valor sorteado sorteado foi {max(numeros)} e o menor valor fo#i {min(numeros)}')# 

#num=(int(input('digite um número:')), int(input('digite outro número:')), int(input('digite mais um número:')), int(input('digite o último número:')))
#print(f'Você digitou os valores {num}')
#print(f'O valor 9 apareceu {num.count(9)} vezes')
#print(f'O valor 3 aparece na {num.index(3)+1}° posição')
#for n in num:
    #if n%2==0:
        #print(f'{n} é par!')



#tupla de listagem de preços:
#listagem=('lápis', 1.75,
#'borracha', 2,
#'estojo', 10,
#'caderno', 16,
#'bolsa', 75,
#'compasso',10,
#'livro', 25)
#print('---'*50)
#print(f'{"LISTAGEM DE PREÇOS":^40}')
#for pos in range(0,len(listagem)):
    #if pos%2==0:
        #print(f'{listagem[pos]:.<30}', end='')
    #else:
        #print(f'R${listagem[pos]:>7.2f}')
#print('---'*50)
#num=[]
#for c in range(0,2):
    #num.append(int(input(f'digite um valor para a posição {c}'))) 
#print(num)



#listas com length escolhida pelo usuáro (não pode cadastrar o mesmo n duas vezes e no final devemos colocar eles em ordem crescente)
#numeros=list()
#while True:
   # n=int(input('digite um valor:'))
    #if n not in numeros:
        #numeros.append(n)
        #print('valor adicionado com sucesso...')
   # else:
        #print('valor duplicado! não vou adicionar.')
    #r=str(input('quer continuar? [S/N]')).strip().upper()
    #if r in 'N':
        #break
#print('-=-=-='*20)
#print(f'você digitou os valores {sorted(numeros)}')


#listingn=[]
#for c in range(0,5):
    #n=int(input('type a number:'))
    #if c==0 or n>listingn[-1]:
        #listingn.append(n)
        #print('adding it to the end of the list')
    #else:
        #pos=0
        #while pos<len(listingn):
            #if n<=listingn[pos]:
                #listingn.insert(pos,n)
                #print(f'adding it to the position {pos}')
                #break
            #pos+=1
#print('-=-=-=-'*20)
#print(f'the numbers typed were {listingn}')
#sei pra onde vai? não

#numbers=[]
#cont=1
#cinco=''
#while True:
    #n=int(input('digite um número:'))
    #numbers.append(n)
    #if n==5:
        #cinco='faz'
    #else:
        #cinco='não faz'
    #cont+=1
    #resp=str(input('quer continuar? [S/N]')).strip().upper()
    #if resp not in 'SN':
        #resp=str(input('tente novamente. quer continuar? [S/N]')).strip().upper()
    #if resp in 'N':
        #break
#print('-=-=-'*20)
#print(f'Você digitou {cont} elementos.')
#numbers.sort(reverse=True)
#print(f'na ordem crescente os números são: {numbers}')
#print(f'o valor 5 {cinco} parte da lista!)


#ler varios numeros e clocar eles em uma lista. depois criar duas listas extras, uma de números pares e uma de impares, e adicionar os valores respectivos. no fim, imprimir as tres listas geradas.



#total=[]
#pares=[]
#impares=[]
#cont=0
#while True:
    #n=int(input('digite um número:'))
    #total.append(n)
    #if n%2==0:
        #pares.append(n)
    #else:
        #impares.append(n)
    #resp=str(input('quer continuar? [S/N]')).strip().upper()[0]
    #if resp not in 'SN':
        #resp=str(input('ERRO! tente novamente. quer continuar? [S/N]')).strip().upper()[0]
    #if resp in 'N':
        #break
#print('=-=-=-='*20)
#print(f'a lista com todos os valores ficou= {total}, a que contém apenas os pares={pares}, a dos impares={impares}')



#numbers=[[],[]]
#for c in range(0,5):
    #n=int(input('digite um número:'))
    #if n%2==0:
        #numbers[0].append(n)
    #else:
        #numbers[1].append(n)
#print(f'os pares foram:{numbers[0]} e os impares foram {numbers[1]}')

#estado=dict()
#brasil=list()
#for c in range (0,2):
    #estado['uf']=str(input('digite o nome do estado: '))
    #estado['sigla']=str(input('digite a sigla do estado: '))
    #brasil.append(estado.copy())
#for e in estado:
    #for k in e.values():
        #print(f'k significa {k} ')
#brasil=[{'uf':   ,'sigla'    },{'uf':   ,'sigla'    },{'uf':   ,'sigla'    }]
#key and value

#pede nome e media, print nome, media e situação (aprovado ou reprovado)
#tudo=[]
#situacao={}
#situacao['aluno']=str(input('nome: '))
#situacao['media']=float(input('média: '))
#while situacao['media']<0:
    #situacao['media']=float(input('Tente novamente. Média: '))
#if 5<=situacao['media']<7:
    #situacao['situacaoatual']='EM RECUPERAÇÃO'
#if situacao['media']<5:
    #situacao['situacaoatual']='REPROVADO(A)'
#else:
    #situacao['situacaoatual']='APROVADO(A)'
#print(f'o(a) aluno(a)  {situacao['aluno']}, de média {situacao['media']} está {situacao['situacaoatual']}')
#print(situacao)
#for k,v in situacao.items():
    #print(f'{k} é igual a {v}')


from random import randint
from time import sleep
from operator import itemgetter
jogo={
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
ranking=[]
print('valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)  
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True) 
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)