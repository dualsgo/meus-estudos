# 2.6.11 LAB Operadores e Expressões – 2
# Cenário

# Sua tarefa é preparar um código simples capaz de avaliar a hora de término de um período, dado como um número de minutos (pode ser arbitrariamente grande). A hora de início é fornecida como um par de horas (0..23) e minutos (0..59). O resultado deve ser impresso no console.

# Por exemplo, se um evento começa às 12:17 e dura 59 minutos, termina às 13:16.

# Não se preocupe com imperfeições no código - tudo bem se ele aceitar um tempo inválido - o mais importante é que o código produz resultados válidos para dados de entrada válidos.

# Teste seu código com cuidado. Dica: usar o operador % pode ser a chave para o sucesso.

# Dados de teste
# Exemplo de entrada:
# 12
# 17
# 59
horas = -1
minutos = -1

while 0 > horas or horas > 23:
	horas = int(input("Hora de início (horas): "))

while 0 > minutos or minutos > 59:
	minutos = int(input("Hora de início (minutos): "))

print(f'São {horas}:{minutos}')

tempo = int(input("Duração do evento (minutos): "))
print(f'O evento tem duração de {tempo} minutos.')

# Escreva seu código aqui.

minutos = (minutos + tempo) % 60
horas += (minutos + tempo) // 60
if horas == 24:
	horas = 0
elif horas > 23:
	horas -= 24
print(f'O evento terminará às {horas}h e {minutos}min')