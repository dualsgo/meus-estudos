# Exercício Python #029 - Radar eletrônico - Aula 00 até 09 - Mundo 1
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint
from time import sleep
from emoji import emojize
# Tarefa 1: Ler a velocidade do carro.
velocidade = randint(40, 110)
print(f'RADAR: Sua velocidade é de {velocidade}Km/h')

velocidade_maxima = 80

# Tarefa 2: Definir o valor da multa
if velocidade > velocidade_maxima:
    print('Você foi multado!')

    acima_do_limte = velocidade - velocidade_maxima
    multa = acima_do_limte * 7

# Tarefa 3: Mostrar a mensagem dizendo se foi multado ou não
    print(f'O limite de velocidade é de 80Km/h. Você foi flagrado a {velocidade}Km/h.')
    print(f'O valor da multa é de R$ 7,00 por Km/h ultrapassado. Sua multa será de R$ {multa:.2f} por trafegar a {acima_do_limte}Km/h além do permitido.')
else:
    print('Você está dentro do limite permitido!')

# EXTRA

print(emojize(':estrada: RADAR ELETÔNICO', language='pt'))
while True:
	try:
		simulações = int(input('Quantas simulações deseja realizar? '))
		break
	except ValueError:
		print('Valor inválido!')

for carro in range(1, simulações+1):
	velocidade = randint(70, 90)

	multado = velocidade - 80 <= 0

	valor = 7 * (velocidade - 80)
	moeda = str(f'{valor:.2f}').replace('.',',')

	print(emojize(f'{f':carro: Veículo {carro} - Velocidade registrada:':<30}{f'{velocidade}Km/h':>20}', language='pt'))

	print(emojize(f'\033[1;32mTenha um bom dia. Dirija com segurança.\033[m' if multado else f'\033[1;31m:sirene: Você foi multado em R$ {moeda} por ultrapassar em {valor/7}Km a velocidade permitida.\033[m', language='pt'))

	sleep(1)
print('Simulações encerradas!')

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