# Exercício Python #096 - Função que calcula área - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
from emoji import emojize
def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(emojize(f'O terreno de largura {largura}m e comprimento {comprimento}m possui uma área de {area_terreno}m²'))

print(emojize(f':régua_reta:{"Controle de terrenos":^30}:régua_reta:', language='pt'))
print()
area(float(input(emojize(':régua_reta: Digite a largura do terreno em m: ', language='pt'))), float(input(emojize(':régua_reta: Digite o comprimento do terreno em m: ', language='pt'))))