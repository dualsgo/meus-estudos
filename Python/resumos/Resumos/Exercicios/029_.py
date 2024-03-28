# Criar sistema de radar eletrônico que verifique a velocidade e aplique multas R$ 7,00 a cada Km excedido e pontos na carteira - Verificar niveis de gravidade da multa

# Infração leve - 3 Pontos - Multa - R$ 5,00 por KM excedido - 10km acima
# Infração moderada - 4 Pontos - Multa - R$ 10,00 por KM excedido - 20km acima
# Infração grave - 6 Pontos - Multa - R$ 15,00 por KM excedido - 30km acima
# Infração gravíssima - 7 Pontos - Multa - R$ 20,00 por KM excedido - 30km+ acima

from random import randint

def verifica(v):
	excedido = v - 80  # Calcula as multas
	acima_limite = (v - 80) > 0  # Verifica se está acima do limite
	multa = (
		excedido * 5 if excedido <= 10 else
		10 if excedido <= 20 else
		15 if excedido <= 30 else 20)  # Define o multiplicador dependendo do grau
	grau = (
		'\033[32mLeve\033[m' if excedido <= 10 else
		'\033[34mModerada\033[m' if excedido <= 20 else
		'\033[33mGrave\033[m' if excedido <= 30 else '\033[31mGravíssima\033[m')
	pontos = (
		3 if excedido <= 10 else
		4 if excedido <= 20 else
		6 if excedido <= 30 else 7)  # Define o multiplicador dependendo do grau

	if acima_limite:

		print(
			f'{'-' * 26}\n'
			f'{'Velocidade:':<11}{v:>13}{'km':<2}\n'
			f'{'Infração:':<11}{grau:>23}\n'
			f'{'Excedido:':<11}{excedido:>13}{'km':>2}\n'
			f'{'Pontos:':<11}{pontos:>15}\n'
			f'{'Multa:':<11}{'R$':>5}{multa:>10.2f}\n'
			f'{'-' * 26}')


for veículos in range(6):
	velocidade = randint(60, 200)  # Define as velocidades
	verifica(velocidade)