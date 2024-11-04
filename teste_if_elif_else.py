nome = input('insira seu nome: ')
idade = int(input('insira sua idade '))
if idade >= 60:
    print(f'{nome} é idoso')
elif idade >= 18:
    print(f'{nome} é adulto!')
elif idade >= 12:
    print(f'{nome} é adolecente!')
else:
    print('{nome} é criança')