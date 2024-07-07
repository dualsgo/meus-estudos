# Exercício Python #061 - Progressão Aritmética v2.0
# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

while True:
    try:
        primeiro_termo = int(input('Digite o primeiro termo: '))
        razão = int(input('Digite a razão da progressão: '))
        acumulador = primeiro_termo
        contador = 0
    except ValueError:
        print(f'Valor de um tipo inválido para essa operação.')

    else:

        while contador < 10:
            print(f'{acumulador}', end=' ⮕ ' if contador < 9 else ' FIM!')
            acumulador += razão
            contador += 1

        break