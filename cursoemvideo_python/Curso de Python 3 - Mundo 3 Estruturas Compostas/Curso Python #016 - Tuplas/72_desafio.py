# Exercício Python #072 - Número por Extenso - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Tupla contendo os números de 0 a 20 por extenso
contagem_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Loop principal
while True:
    # Solicita ao usuário que digite um número entre 0 e 20
    numero = int(input('Digite um número: 0 até 20 '))

    # Verifica se o número está dentro do intervalo permitido
    if 0 <= numero <= 20:
        # Imprime o número por extenso
        print(f'O número {numero} por extenso é {contagem_por_extenso[numero]}.')

        # Pergunta ao usuário se deseja continuar
        continuar = str(input('Continuar? S/N ')).strip().upper()

        # Se a resposta não for 'S', encerra o loop
        if continuar not in 'Ss':
            break
    else:
        # Se o número não estiver no intervalo permitido, solicita que o usuário tente novamente
        print('Tente novamente.')



