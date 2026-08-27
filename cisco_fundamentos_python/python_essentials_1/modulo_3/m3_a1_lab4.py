# 3.1.12 LAB Essenciais da declaração if-elif-else
# Cenário

# Como você certamente sabe, devido a algumas razões astronômicas, os anos podem ser bissextos ou comuns. Os primeiros têm 366 dias, enquanto os segundos têm 365 dias.

# Desde a introdução do calendário gregoriano (em 1582), a regra a seguir é usada para determinar o tipo de ano:

# se o número do ano não é divisível por quatro, é um ano comum;
# caso contrário, se o número do ano não for divisível por 100, será um ano bissexto;
# caso contrário, se o número do ano não for divisível por 400, é um ano comum;
# caso contrário, é um ano bissexto.

# O código deve gerar uma das duas mensagens possíveis: se o ano é bissexto ou ano comum, dependendo do valor inserido.

# Seria bom verificar se o ano inserido cai na era gregoriana e emitir um aviso caso contrário: não está dentro do período do calendário gregoriano. Dica: use os operadores '!=' E '%'.

ano = int(input('Digite um ano: '))

if ano >= 1582:
	print('Ano dentro do calendário Gregoriano (1582 - atualmente)')
	if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
		print(f'O ano de {ano} é um ano bissexto!')
	else:
		print(f'O ano de {ano} é um ano comum!')
else:
	print('Ano fora do calendário Gregoriano (anterior a 1582).')