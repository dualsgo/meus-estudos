# MIMO - 13 - Módulos e Bibliotecas - Desafio 2

# Como parte da pesquisa para um artigo que está escrevendo, Mia criou um programa para obter o preço médio dos imóveis residenciais em uma área. O programa dela funciona bem, mas como ela está usando apenas uma função, não precisamos importar todo o módulo statistics . Altere sua instrução de importação para importar apenas a função median do módulo statistics . Em seguida, remova statistics ao usar a função median .

from statistics import median

prices = [300000, 270000, 389000, 295000, 321000, 288000, 232000, 200000,323000]
result = median(prices)
print(f"Median property price for the area is ${result}")