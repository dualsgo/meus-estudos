# 3.2.15   LAB   A hipótese de Collatz
# Cenário

# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:

# pegue qualquer número inteiro diferente de zero e nomeie-o c0;
c0 = int(input('Digite um número inteiro diferente de zero: ')) # Recebe o valor de c0
contador = 0 # Contador de etapas para chegar a 1
while True:
  # se c0 for par, avalie um novo c0 como c0 ÷ 2; se não for par, só pode ser ímpar, então ele recebe uma nova avaliação: 3 × c0 + 1;
	if c0 % 2 == 0: # Se o resto da divisão de c0 por 2 for 0, então é par
		c0 = c0 / 2  # c0 recebe o valor de c0 dividido por 2
		contador += 1 # Contador de etapas aumenta em 1
		print(f'Etapa {contador}: {int(c0)}') # Imprime o valor de c0
	else:
	# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
		if c0 != 1: # Se c0 for diferente de 1
			c0 = 3 * c0 + 1 # c0 recebe o valor de 3 * c0 + 1
			contador += 1 # Contador de etapas aumenta em 1
		else: # Se c0 for igual a 1,
			break # sai do loop
		print(f'Etapa {contador}: {int(c0)}') # Imprime o valor de c0

# se c0 ≠ 1, volte ao ponto 2.
print(f'Foram {contador} etapas')

# A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.
# Obviamente, é uma tarefa extremamente complexa usar um computador para provar a hipótese de qualquer número natural (pode até exigir inteligência artificial), mas você pode usar o Python para verificar alguns números individuais. Talvez você até encontre aquele que refutaria a hipótese.

# Escreva um programa que leia um número natural e execute as etapas acima, desde que c0 permaneça diferente de 1. Também queremos que você conte as etapas necessárias para atingir o objetivo. Seu código deve gerar todos os valores intermediários de c0 também.