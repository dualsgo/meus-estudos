# Exercício Python #101 - Funções para votação - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import  datetime
def voto(ano_nascimento):
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f'\033[1;31mCOM {idade} ANOS O NÃO VOTA\033[m'
    else:
        if 18 <= idade <= 65:
            return f'\033[1;33mCOM {idade} ANOS O VOTO É OBRIGATÓRIO\033[m'
        else:
            return f'\033[1;32mCOM {idade} ANOS O VOTO É OPCIONAL\033[m'


ano_nascimento = int(input('Digite o seu ano de nascimento: '))

print(voto(ano_nascimento))