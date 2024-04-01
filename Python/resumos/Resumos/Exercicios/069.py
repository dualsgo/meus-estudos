# Exercício Python #069 - Análise de dados do grupo
# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mais_18 = 0
homens = 0
mulheres = 0

while True:
	try:
		print(f'{'-' * 20}\nCADASTRE UMA PESSOA\n{'-' * 20}')
		idade = int(input('Idade: '))
		sexo = input('Sexo: ').strip().upper()
		if idade > 18:
			mais_18 += 1
		if sexo == 'M':
			homens += 1
		if idade > 20 and sexo == 'F':
			mulheres += 1

	except ValueError:
		continue

	try:
		continuar = input('Continuar? S/N').strip().upper()
		if continuar == 'N':
			break
		elif continuar == 'S':
			continue
	except Exception as e:
		print(e)

print(f'Pessoas com mais de 18 anos: {mais_18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com mais de 20 anos: {mulheres}')