print('vamos calcular equação de segundo grau que legal :(')
a = float(input('Escreva o primeiro numero '))
b = float(input('Escreva o segundo numero '))
c = float(input('Escreva o terceiro numero '))
delta = b**2 - 4*a*c
if delta < 0:
    print('Nenhuma solução real')
elif delta == 0:
    print('Uma solução real')
else:
    print('Duas soluções reais')