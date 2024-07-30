# Exercício Python #072 - Número por Extenso - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
	try:
		print(f"Você digitou o número {extenso[int(input('Digite um valor entre 0 e 20: '))]}")
		continuar = str(input('Continuar? S/N ')).strip().upper()
		if continuar not in 'Ss':
			break
	except IndexError:
		print('Somente valores entre 0 e 20')
	except ValueError:
		print('Apenas valores numéricos.')

# Versão 2

numeros_por_extenso = (
	'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
	'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
	'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
	'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
	try:
		numero = int(input('Digite um valor entre 0 e 20: '))
		if 0 <= numero <= 20:
			break
		else:
			print("Inválido")
	except ValueError:
		print('Este valor é de um tipo de dado inválido para essa operação!')

resultado = f'O número {numero} por extenso é: {numeros_por_extenso[numero]}'
tamanho = len(resultado)
print(resultado)
print(f'{"-" * tamanho}')