# Exercício Python #004 - Dissecando uma Variável
# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ').strip()

if algo.isnumeric():
    converter = int(algo)
    print(f'{converter} é um valor do tipo {type(converter).__name__}')
else:
    try:
        converter = float(algo)
        print(f'{converter} é um valor do tipo {type(converter).__name__}')
    except ValueError:
        print(f'{algo} é um valor do tipo {type(algo).__name__}')


"""print('Lista de métodos válidos:')
for i in dir(algo):
	if '_' not in i:
		print(f"{'.' + i + '()'}")
		"""