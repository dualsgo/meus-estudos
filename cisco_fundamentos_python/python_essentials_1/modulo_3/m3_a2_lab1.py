from random import randint
# 3.2.4 LAB Adivinhe o número secreto
# Cenário
# Um jovem mágico escolheu um número secreto. Ele o ocultou em uma variável chamada secret_number.
# Ele quer que todos que executam seu programa jogue o jogo Adivinhe o número secreto e adivinhem qual número ele escolheu para eles.
# Quem não adivinhar o número ficará para sempre em um loop infinito! Infelizmente, ele não sabe como completar o código.
print("""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""") 	# A maneira como usamos aqui é chamada de impressão de várias linhas. Você pode usar aspas triplas para imprimir sequências de caracteres em várias linhas para facilitar a leitura ou criar um design especial baseado em texto.
# Sua tarefa é ajudar o mágico a preencher o código no editor de forma que o código:
secret_number = randint(0, 999)
# solicitará que o usuário insira um número inteiro;
user = int(input())
# Vai usar um while loop;
while True:
	# Verificará se o número inserido pelo usuário é igual ao número escolhido pelo mágico.
	if user == secret_number:
		# Se o número inserido pelo usuário corresponder ao número escolhido pelo mago, ele deverá ser impresso na tela, e o mago deve dizer as seguintes palavras: "Muito bem, trouxa! Você está livre agora."
		print("Muito bem, trouxa! Você está livre agora.")
		break
	else:
		print("Ha ha! Você está preso no meu loop!")
		if secret_number > user:
			print('Dica: É maior!')
		elif secret_number < user:
			print('Dica: É menor!')
		# Se o número escolhido pelo usuário for diferente do número secreto do mago, o usuário deverá ver a mensagem "Ha ha! Você está preso no meu loop!" E será solicitado a inserir um número novamente.
		user = int(input('Digite outro número: '))