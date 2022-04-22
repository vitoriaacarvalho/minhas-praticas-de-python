from time import sleep
pessoa={}
pessoa['nome']=str(input('Nome: '))
while len(pessoa['nome']) <=1 or type((pessoa['nome']))!=str :
    pessoa['nome']=str(input('ERRO! Tente novamente, com um nome válido. Nome: '))
pessoa['anonasc']=int(input('Ano de Nascimento:'))
while pessoa['anonasc']<1900 or pessoa['anonasc']>=2022:
    pessoa['anonasc']=int(input('ERRO! Digite um ano válido. Ano de Nascimento:'))
pessoa['carteira']=int(input('Carteira de trabalho [0=não tenho]:'))
while pessoa['carteira']<1000000 and (pessoa['carteira'])!=0:
    pessoa['carteira']=int(input('ERRO! Digite um número válido. Carteira de trabalho [0=não tenho]:'))
pessoa['sexo']=str(input('Qual o seu sexo? [feminino/masculino]')).strip().upper()[0]
while pessoa['sexo'] not in 'MF' or type((pessoa['sexo']))!=str:
    pessoa['sexo']=str(input('ERRO. Tente novamente: qual o seu sexo? [feminino/masculino]')).strip().upper()[0]
if pessoa['sexo'] in 'M':
    sexo='cadastrado'
else:
    sexo='cadastrada'
pessoa['anocontratacao']=int(input(f'Digite o ano que você foi {sexo}'))
while pessoa['anocontratacao']<2010 or pessoa['anocontratacao']>2022:
#2010=ano de criação da empresa
    pessoa['anocontratacao']=int(input(f'ERRO! Digite um número válido. Digite o ano que você foi {sexo}'))
pessoa['salario']=int(input('Salário:'))
while pessoa['salario']<=0:
    pessoa['salario']=int(input('ERRO! digite um salário válido:'))
print('=-=-=-'*20)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
    sleep(1)

#fiz uma validação de dados completa nesse! <3