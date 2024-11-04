nome = input('digite seu nome ')
idade = int(input('digite a sua idade '))
assert idade >= 0, 'Erro: idade menor que zero!' #função para dar erro
#if idade < 0:
    #print(f'idade invalida')
    #exit()
if idade >= 18:
    print(f'{nome} já é maior de idade')

    if idade >= 40:
        print(f'já está um pouco velho não?')
else:
    print(f'{nome} não é maior de idade pois só tem {idade}')
print(f'{nome} tem {idade} anos de idade')