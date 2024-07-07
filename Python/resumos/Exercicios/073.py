# Exercício Python #073 - Tuplas com Times de Futebol
# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

classificacao_final_brasileirao_2023 = (
    "Palmeiras",
    "Grêmio",
    "Atlético-MG",
    "Flamengo",
    "Botafogo",
    "RB Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco da Gama",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG",
)


for pos, time in enumerate(classificacao_final_brasileirao_2023, 1):
	if pos < 5:
		print(f'\033[1;32m{pos:<2} - {time:<15}\033[m')
	elif pos < 7:
		print(f'\033[1;33m{pos:<2} - {time:<15}\033[m')
	elif pos < 13:
		print(f'\033[1;34m{pos:<2} - {time:<15}\033[m')
	elif pos < 17:
		print(f'\033[1;m{pos:<2} - {time:<15}\033[m')
	else:
		print(f'\033[1;31m{pos:<2} - {time:<15}\033[m')