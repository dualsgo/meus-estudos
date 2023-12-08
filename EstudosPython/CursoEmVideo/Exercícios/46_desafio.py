# Exercício Python #046 - Contagem regressiva - Aula 00 até 13 - Mundo 2
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Tarefa 1: Importar os módulos
from time import sleep
from emoji import emojize
fogos = ':fogos_de_artifício:'
print('CONTAGEM REGRESSIVA!')
# Tarefa 2: Criar a contagem regressiva
for contagem_regressiva in range(10, -1, -1):
    print(emojize(f':tecla_{contagem_regressiva}:', language='pt'))
    sleep(1)

print(emojize(f'{fogos * 10}', language='pt'))
