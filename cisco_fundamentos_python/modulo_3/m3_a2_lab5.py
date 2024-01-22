# 3.2.14 LAB Essenciais do loop while
# Cenário

# Ouça esta história: um garoto e seu pai, um programador de computador, estão jogando com blocos de madeira.
# Eles estão construindo uma pirâmide. A pirâmide deles é um pouco esquisita, pois, na verdade, é uma parede em forma de pirâmide - é plana.
# A pirâmide é empilhada de acordo com um princípio simples: cada camada inferior contém um bloco a mais do que a camada acima.

# Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída usando esses blocos.

# Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente.

blocos = int(input("Insira o número de blocos:")) # Recebe o número de blocos
andar = 0 # Contador de andares
andar_atual = 1 # Contador de blocos no andar_atual
while True: # Loop infinito
	if blocos >= andar_atual: # Se o número de blocos for maior ou igual ao número de blocos no andar_atual que é igual a 1
		andar += 1 # Contador de andares aumenta em 1
		blocos -= andar_atual # Número de blocos recebe o valor de blocos menos o número de blocos no andar_atual, ou seja, o número de blocos restantes
		andar_atual += 1 # Número de blocos no andar_atual aumenta em 1, pois a próxima camada terá um bloco a mais
		print(f'Blocos restantes {blocos}')
	else:
		break

print(f'Altura da pirâmide: {andar}')