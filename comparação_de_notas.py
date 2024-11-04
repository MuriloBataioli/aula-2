print('Vamos ver se você passou de ano ou não')
nota1 = float(input('Qual é a primeira nota? '))
nota2 = float(input('Qual é a segunda nota? '))
nota3 = float(input('Qual é a terceira nota? '))
print('Qual é o peso das provas?')
peso1 = float(input('Qual é o peso da primeira prova? '))
peso2 = float(input('Qual é o peso da segunda prova? '))
peso3 = float(input('Qual é o peso da terceira prova? '))
mf = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1 + peso2 + peso3)
if mf < 5.0:
    print('REPROVADO')
elif mf >= 5.0 and mf <= 7.0:
    print('prova final')
elif mf >= 7.1:
    print('aprovado')
print(f'{mf}')