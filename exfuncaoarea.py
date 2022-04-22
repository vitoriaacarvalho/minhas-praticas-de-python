#tenha uma função area e receba as dimensões de um terreno retangular (largura e comprimento) e mostre a area do terreno.
def area(a,b):
    calArea=(a+b)/2
    print(f'A área total desse terreno de {a}x{b} é {calArea}m²')

a=int(input('digite a largura do terreno:'))
b=int(input('digite o comprimento do terreno:'))
area(a,b)