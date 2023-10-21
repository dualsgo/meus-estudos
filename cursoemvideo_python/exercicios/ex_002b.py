"""Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada."""

# Passo 1: Criar as variáveis que irão armazenar os dados solicitados (dia, mês e ano) utilizando a função input para permitir que o usuário digite os dados.
dia = input('\033[1;47mDigite o dia do seu nascimento:\n\t\033[m')
mes = input('\033[1;47mAgora digite o mês:\n\t\033[m')
ano = input('\033[1;47mPor fim, digite o seu ano de nascimento:\n\t\033[m')

# Passo 2: Com os dados armazenados nas variáveis, utilizamos a função print() para exibir o resultado em uma string formatada.
print(f'\033[1;31mVocê nasceu no dia {dia} de {mes} de {ano}. Correto?\033[m')
