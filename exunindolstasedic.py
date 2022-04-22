galera=list()
pessoa=dict()
soma=media=mulheres=0
while True:
    pessoa.clear() 
    pessoa['nome']=str(input('nome: '))
    while True:
        pessoa['sexo']=str(input('sexo [M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'F':
            mulheres+=1
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F')
    pessoa['idade']=int(input('idade:')) 
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('erro! responda apenas com S ou N.')
    if resp=='N':
        break
print('=-=-=-'*20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media=soma/len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'A lista de pessoas que estão cima da média: ')
for p in galera:
    if p['idade']>=media:
        print('  ', end='')
        for k,v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('fim do programa')
