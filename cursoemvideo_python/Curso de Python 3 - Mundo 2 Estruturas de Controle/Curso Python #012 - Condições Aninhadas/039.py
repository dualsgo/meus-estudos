# Exercício Python #039 - Alistamento Militar
# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nascimento = 2006
idade = atual - nascimento
alistamento = idade == 18
status = 'não está no período' if idade < 18 else 'deve se alistar' if idade == 18 else 'passou do período'


if alistamento:
	print(f'Você que completa 18 anos este ano e {status}!')
else:
	if idade < 18:
		print(f'Você tem {idade} anos e {status} de alistamento! Aguarde mais {18-idade} anos, até o ano de {nascimento+18}.')
	else:
		print(f'Você tem {idade} anos e {status} de alistamento! Se não se alistou a {atual-(nascimento+18)} anos, no ano de {nascimento+18}, está irregular com o Serviço Militar!')