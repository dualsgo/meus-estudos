# 2.6.11 LAB Operadores e Expressões – 2
# Cenário

# Sua tarefa é preparar um código simples capaz de avaliar a hora de término de um período, dado como um número de minutos (pode ser arbitrariamente grande). A hora de início é fornecida como um par de horas (0..23) e minutos (0..59). O resultado deve ser impresso no console.

# Por exemplo, se um evento começa às 12:17 e dura 59 minutos, termina às 13:16.

horas = -1
minutos = -1

while horas not in range(0, 24):
	horas = int(input("Hora de início (horas): "))

while minutos not in range(0, 60):
	minutos = int(input("Hora de início (minutos): "))

print(f'São {horas}:{minutos}')

tempo = int(input("Duração do evento (minutos): "))
print(f'O evento tem duração de {tempo} minutos.')

hora_adicional = (minutos + tempo) // 60
minutos = (minutos + tempo) % 60
horas += hora_adicional

if horas > 23:
  hora = horas % 24
  horas = 0
  horas += hora


print(f'O evento terminará às {horas}h e {minutos}min')