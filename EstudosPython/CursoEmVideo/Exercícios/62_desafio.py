# Exercício Python #062 - Super Progressão Aritmética v3.0 - Aula 00 até 14 - Mundo 2
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))  # Solicita e converte o primeiro termo para inteiro
razao = int(input('Digite a razão da PA: '))  # Solicita e converte a razão para inteiro
decimo_termo = razao * 10  # Calcula o décimo termo da PA

resposta = False  # Inicializa a variável de resposta
termo = 0
while not resposta:
    termo += 1

    print(f'{termo}º termo: {primeiro_termo}')  # Exibe o termo atual da PA

    primeiro_termo += razao  # Atualiza o valor do próximo termo
    decimo_termo -= razao  # Reduz o contador do décimo termo
    if decimo_termo == 0:
        pergunta = str(input('Deseja adicionar mais termos? S/N')).strip().upper()  # Pergunta se deseja adicionar mais termos
        if pergunta == 'S':
            print('Quantos?')
            termos = int(input(''))  # Solicita a quantidade de termos adicionais
            decimo_termo = razao * termos  # Calcula o novo décimo termo
            resposta = False
        elif pergunta == 'N':
            print('OK. Encerrando...')
            resposta = True


