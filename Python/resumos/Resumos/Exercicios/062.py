# Exercício Python #062 - Super Progressão Aritmética v3.0
# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

while True:
    try:
        primeiro_termo = int(input('Digite o primeiro termo: '))
        razão = int(input('Digite a razão da progressão: '))
        acumulador = primeiro_termo
        contador = 0
        termos = 10

    except ValueError:
        print(f'Valor de um tipo inválido para essa operação.')
    else:

        while True:
            while contador < termos:
                print(f'{acumulador}', end=' ⮕ ' if contador < termos-1 else ' ⮕ PAUSA\n')
                acumulador += razão
                contador += 1
            mais_termos = int(input('Quantos termos deseja visualizar? '))
            if mais_termos == 0:
                break
            termos += mais_termos

        print(f'Encerrando o programa!')
        break