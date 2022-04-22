def escreva(msg):
    quant=(len(msg))+4
    print('~'*quant)
    print(f'  {msg}')
    print('~'*quant)


msg=str(input('nome/nomes escolhidos:'))
escreva(msg)