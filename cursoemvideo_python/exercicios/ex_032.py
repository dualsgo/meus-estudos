import datetime
"""Desafio 032 - Ano Bissexto (Aula 01 a 10): Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

"""
Anos divisíveis por 4 são candidatos a serem bissextos.
No entanto, se o ano for divisível por 100, ele não será bissexto, a menos que:
O ano também seja divisível por 400, nesse caso, ele é bissexto.
"""
print("""
      \033[7mMétodo com valor digitado\033[m
      """)
# Extra - Pegar ano atual no sistema - Importamos a biblioteca datetime
# Atribuimos a uma variável o método
ano_atual = datetime.datetime.now().year
# Passo 1: Ler o ano - Atribuímos o valor a uma variável através do método input.
print('Digite o ano que deseja saber:')
ano = int(input(''))
print(f'Você digitou {ano}\n')
# Passo 2: Criar a regra para fazer a verificação condicional - (ANOS DIVISÍVEIS POR 4 SÃO BISSEXTOS, EXCETO SE FOREM DIVISÍVEIS TAMBÉM POR 100. SE FOREM DIVISÍVEIS POR 100, PARA SER BISSEXTO DEVE SER DIVISÍVEL POR 400)
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
# Passo 3: Exibir o resultado verificando a condição
if bissexto:
    print(f'\033[1;45m{ano} é BISSEXTO!\033[m')
else:
    print(f'\033[1;43m{ano} não é BISSEXTO!\033[m')

print("""
      \033[7mMétodo com móduto datetime\033[m
      """)
ano_atual_bissexto = (ano_atual % 4 == 0 and ano_atual %
                      100 != 0) or (ano_atual % 400 == 0)

if ano_atual_bissexto:
    print(f'\033[1;45mO ano atual {ano_atual} é bissexto.\033[m')
else:
    print(f'\033[1;43mO ano atual {ano_atual} náo é bissexto.\033[m')
