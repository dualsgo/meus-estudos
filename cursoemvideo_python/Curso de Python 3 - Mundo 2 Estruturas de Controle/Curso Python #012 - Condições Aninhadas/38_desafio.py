# Exercício Python #038 - Comparando números - Aula 00 até 12 - Mundo 2
# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

# Tarefa 1: Ler dois números inteiros
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
maior = menor = primeiro

# Tarefa 2: Verificar se há um maior ou se são iguais
if primeiro != segundo:
    if primeiro > segundo:
        print('O primeiro valor é o maior!')
        maior = primeiro
        menor = segundo
    elif primeiro < segundo:
        print('O segundo valor é o maior!')
        maior = segundo
        menor = primeiro
    print(f'O maior é {maior} e o menor é {menor}')
else:
    print('Os números são iguais!')

# Versão 2 - Simplificada

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

print(
	f'{valor1} é maior que {valor2}' if valor1 > valor2 else
	f'{valor1} é menor que {valor2}' if valor1 < valor2 else
	f'{valor1} e {valor2} são iguais.')

# Versão 3 - Com validação  

def obter_valor(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Tipo de dado inválido para essa operação.')


primeiro = obter_valor('Digite o primeiro valor: ')
segundo = obter_valor('Digite o segundo valor: ')
verificação = 'O primeiro valor é o maior!' if primeiro > segundo else 'O segundo valor é o maior' if primeiro < segundo else 'Os valores são iguais!'
print(verificação)