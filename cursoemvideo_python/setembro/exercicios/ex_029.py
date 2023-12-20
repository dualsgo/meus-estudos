"""Desafio 029 - Radar eletrônico (Aula 01 a 10): Escreva um programa que leia a velocidade de um carro. 

- Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 70,00 por cada Km acima do limite."""

# Passo 1: Escrever um número que leia a velocidade de um carro - Para isso atribuiremos a uma variável o método imput para que o usuário entre com a velocidade. Converteremos o valor para um número inteiro.

print("""\033[1;42mSoy, Francesco Virgolini, Fiiiaaaaaaaaauunn
La máquina más bloz De tote italiee Fiiiaaaa\033[m""")
print('Qual é a sua velocidade?')
velocidade = int(input(''))

# Passo 2: Verificar se a velocidade máxima foi ultrapassada - Primeiro para fins de entendimento definiremos uma variável e atribuimos o valor da velocidade maxima
velocidade_maxima = 80
# Depois faremos a estrutura condicional usando a comparação

if velocidade > velocidade_maxima:  # Se a velocidade for maior que a permitida...
    # Mostra a mensagem informando sobre a multa
    print('\033[1;31mVOCÊ FOI MULTADO!\033[m')

    # Calcularemos o valor da multa dentro da estrutura condicional no bloco True
    # Primeiro calculamos a diferença para saber o valor excedido
    multa = velocidade - velocidade_maxima
    # A multa será de R$ 70,00 a cada Km exedido
    multa = multa * 70
    # Exibiremos a mensagem com o valor a ser pago
    print(f'O valor da sua multa é \033[1;32mR$ {multa:.2f}\033[m.')

else:  # Se a velocidade for menor, apenas mostra uma mensagem de saudação
    print('\033[1;32mRespeite as leis de trânsito! Boa viagem.\033[m')
