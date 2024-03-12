# Exercício Python #111 - Transformando módulos em pacotes - Aula 00 até 22 - Mundo 3
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from pacoteexercicios import utilidadescev

valor = int(input('Digite um valor: '))
escolhendo = int(input(f"""Qual função deseja realizar?
[1] Aumentar
[2] Diminuir
[3] Dobrar
[4] Dividir pela metade
[5] Formato monetário
"""))

print(f'O resultado é {utilidadescev.escolha(escolhendo, valor)}')