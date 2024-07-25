# Exercício Python #049 - Tabuada v.2.0 - Aula 00 até 13 - Mundo 2
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Tarefa 1: Solicitar o número que deseja verificar a tabuada
numero = int(input('Digite o número que deseja ver a tabuada: '))

# Tarefa 2: Criar a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i:2} = {resultado:2}')
