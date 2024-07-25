# Exercício Python #061 - Progressão Aritmética v2.0 - Aula 00 até 14 - Mundo 2
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))  # Solicita e converte o primeiro termo para inteiro
razao = int(input('Digite a razão da PA: '))  # Solicita e converte a razão para inteiro
decimo_termo = razao * 10  # Calcula o décimo termo da PA
termo = 0

while decimo_termo > 0:
    termo += 1
    print(f'{termo:2}º termo: {primeiro_termo:2}')  # Exibe o termo atual da PA

    primeiro_termo += razao  # Atualiza o valor do próximo termo
    decimo_termo -= razao  # Reduz o contador do décimo termo

