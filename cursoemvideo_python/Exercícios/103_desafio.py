# Exercício Python #103 - Ficha do Jogador - Aula 00 até 21 - Mundo 3
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=0, gols=0):
    if nome == '':
        nome = 'Não informado'
    if gols == '':
        gols = 'Não informado'
    return f'Nome: {nome}\nGols marcados: {gols}'

n = str(input('Digite o nome do jogador: ')).strip().capitalize()
g = input(f'Digite a quantidade de gols marcados por {n}: ')
if g.isnumeric():
    g = int(g)
else:
    g = ''

print(f'Informações do jogador')
print(ficha(n, g))