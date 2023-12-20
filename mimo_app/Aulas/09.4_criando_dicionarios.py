# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.4 - Criando dicionários

# A sede desta marca fica em New York e a loja principal em Paris, mas não podemos dizer apenas olhando locations_list

locations_list = ['New York', 'Paris']

# Para associar significado a cada valor em uma coleção de valores, usamos uma estrutura de dados chamada dicionário.
# Para criar um dicionário, começamos codificando um par de chaves

locations = {
    'headquarters': 'New York',
    'flagship': 'Paris'
}

# Os dicionários são compostos de pares de chaves, e valores, separados por dois pontos.

# As chaves são como índices rotulados. Nós usamos porque nos ajudam a recuperar valores como 'Paris' com base no seu significado.
# Só podemos usar uma chave por vez. Cada chave está associada a um valor

# Dentro do dicionário, separamos pares de valores-chave com vírgulas

# As chaves de um dicionário podem ser números, boolean ou tuplas, mas o tipo mais comumente usado é string. Os valores podem ser de qualquer tipo, inclusive listas.

# Podemos armazenar quantos pares de valores-chave quisermos dentro de um dicionário.

