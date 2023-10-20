"""Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada."""

# Passo 1: Criar as variáveis que irão armazenar os dados solicitados (dia, mês e ano) utilizando a função input para permitir que o usuário digite os dados.
dia = input('Digite o dia do seu nascimento: ')
mes = input('Agora digite o mês: ')
ano = input('Por fim, digite o seu ano de nascimento: ')

# Passo 2: Com os dados armazenados nas variáveis, utilizamos a função print() para exibir o resultado em uma string formatada.
print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto?')
