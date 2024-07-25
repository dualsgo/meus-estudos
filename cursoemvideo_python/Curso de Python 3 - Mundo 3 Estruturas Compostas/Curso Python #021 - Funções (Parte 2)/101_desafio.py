# Exercício Python #101 - Funções para votação - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import datetime  # A importação também tem escopo global ou local
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    verificacao = "PODE VOTAR!" if idade >= 16 else "NÃO PODE VOTAR!"
    print(f'Com {idade} anos você {verificacao}')
    if 'NÃO' in verificacao:
        print(f'Faltam {16 - idade} anos')
    else:
        print(f'Seu voto obrigatório!' if 18 <= idade <= 70 else 'Seu voto é facultativo!')


ano_nascimento = int(input('Digite o seu ano de nascimento: '))
voto(ano_nascimento)