from time import sleep
time=[]
player={}
partidas=[]
cont=0
player['nome']=str(input('nome:'))
tot=int(input(f'quantas partidas {player["nome"]} jogou?'))
for c in range (0,tot):
    partidas.append(int(input(f'      Quantos  gols na partida {c}?')))
player['gols']=partidas[:]
player['total']=sum(partidas)
print(player)
for k,v in player.items():
    print(f'o campo {k} tem o valor de {v}')
print(f'o jogador {player["nome"]} jogou {len(jogador["gols"])} partidas')

