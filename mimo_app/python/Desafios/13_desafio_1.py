# MIMO - 13 - Módulos e Bibliotecas - Desafio 1

# Ricky está fazendo um projeto de matemática. Ele está tentando criar um conversor de radianos e graus usando Python, mas esqueceu de importar o módulo. Ajude Ricky a importar o pacote math.

import math

def degree_to_radian(degree):
    print(f'{degree} degree = {math.radians(degree)} radian')

def radian_to_degree(radian):
    print(f'{radian} radian = {math.degrees(radian)} degree')

degree_to_radian(90)
radian_to_degree(0.785)