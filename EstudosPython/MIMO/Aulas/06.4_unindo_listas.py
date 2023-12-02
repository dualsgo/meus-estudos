# MIMO - 06 - Operações com listas
# 06.4 - Unindo listas de dados

# Frequentemente encontraremos diferentes conjuntos de dados que devemos combinar em um só, como o valor das vendas no fim de semana.
sabado = [50, 3, 20, 22, 5]
print(sabado)
domingo = [60, 10, 9, 11, 40]
print(domingo)

# Para combinar dois conjuntos de dados, criamos uma expressão usando o operador +. A segunda lista é anexada no final da primeira. Podemos salvar alista combinada em uma variável para reutiliza-la
vendas_fds = sabado + domingo
print(vendas_fds)

# A união também funciona com diferentes tipos de valores.
