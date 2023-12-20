"""Desafio 067 - Tabuada v3.0 (Aula 01 a 15): Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O progamara será interrompido quando o número solicitado for negativo.
"""
# Inicializa o contador
contador = 1

# Recebe o primeiro valor
numero = int(input('Gostaria de ver a tabuada de qual número? '))

# Inicia o loop infinito
while True:
    # Antes verifica se o valor é negativo
    if numero < 0:
        # Se for, para o programa!
        print('Só funcionamos com números positivos! Encerrando o programa.')
        break
    # Se não for, segue o fluxo e exibe a tabuada até 10
    print(f'{numero:2} x {contador:2} = {numero * contador:2}')

    # Atualiza o contador a cada loop (até 10)
    contador += 1

    # Quando o contador chega na 11 iteração, pergunta se deseja verificar outra tabuada
    if contador == 11:
        print('Deseja ver outra tabuada? S/N')
        resposta = str(input('')).upper().strip()

        # Se sim, solicitar o valor e reinicia o contador
        if resposta == 'S':
            numero = int(input('Então digite o próximo número: '))
            contador = 1
        # Se não, para o programa
        else:
            break

# Exibe mensagem de encerramento
print('Programa tabuada encerrado!')

