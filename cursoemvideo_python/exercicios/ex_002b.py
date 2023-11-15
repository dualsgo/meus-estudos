"""Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada."""

# Passo 1: Criar as variáveis que irão armazenar os dados solicitados (dia, mês e ano) utilizando a função input para permitir que o usuário digite os dados.

dia = int(input('\033[1;47mDigite o dia do seu nascimento:\033[m\n'))
mes = int(input('\033[1;47mAgora digite o mês:\033[m\n'))
ano = int(input('\033[1;47mPor fim, digite o seu ano de nascimento:\033[m\n'))

# Passo 2: Com os dados armazenados nas variáveis, utilizamos a função print() para exibir o resultado em uma string formatada.
print(f'\033[1mSua data de nascimento é: \033[1;31m{dia}/{mes}/{ano}\033[m.\n\033[1mCorreto?\033[m')
