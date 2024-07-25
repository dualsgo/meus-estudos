# 3.1.11 LAB Essenciais da declaração if-else
# Cenário

# Era uma vez uma terra - uma terra de leite e mel, habitada por pessoas felizes e prósperas. As pessoas pagavam impostos, é claro - a felicidade tinha limites. O imposto mais importante, chamado de imposto de renda pessoal (PIT) tinha que ser pago uma vez por ano sendo avaliado usando a seguinte regra:

# se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)

# se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.

# Sua tarefa é escrever uma calculadora de impostos.

# Ela deve aceitar um valor de ponto flutuante: a receita.
# Em seguida, ele deve imprimir o imposto calculado, arredondado para inteiro. Há uma função chamada round() que fará o arredondamento para você - você a encontrará no código do esqueleto no editor.

# Nota: esse país feliz nunca devolveu dinheiro para seus cidadãos. Se o imposto calculado for menor que zero, isso significaria apenas nenhum imposto (o imposto foi igual a zero). Leve isso em consideração durante os cálculos.

receita = float(input('Digite o valor da sua renda: R$ '))
if receita <= 85528.00:
	imposto = (receita * .18) - 556.02
	if imposto <= 0:
		print('Não haverá cobrança.')
	else:
		print(f'Para a receita de {receita:.2f} o valor do imposto é R$ {imposto:.2f}')
else:
	ex = receita - 85528.00
	imposto = 14839.02 + (ex * .32)
	if imposto <= 0:
		print('Não haverá cobrança.')
	else:
		print(f'Para a receita de {receita:.2f} o valor do imposto é R$ {imposto:.2f}')