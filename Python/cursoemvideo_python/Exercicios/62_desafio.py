# Exercício Python #062 - Super Progressão Aritmética v3.0 - Aula 00 até 14 - Mundo 2
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# Solicita e converte o primeiro termo da PA para inteiro
primeiro_termo = int(input('Digite o primeiro termo da PA: '))

# Solicita e converte a razão da PA para inteiro
razao = int(input('Digite a razão da PA: '))

enesimo = int(input('Quantos termos deseja visualizar inicialmente? '))

# Calcula o enésimo termo da PA
enesimo_termo = razao * enesimo

# Inicializa a variável de resposta
resposta = False
termo_atual = 0
termos_exibidos = 0
print(f'Exibindo os {enesimo} termos iniciais...')

# Loop para exibir os termos da PA
while not resposta:
    termo_atual += 1
    termos_exibidos += termo_atual

    # Exibe o termo atual da PA
    print(f'{termo_atual}º termo: {primeiro_termo}')

    # Atualiza o valor do próximo termo
    primeiro_termo += razao

    # Reduz o contador do enésimo termo
    enesimo_termo -= razao

    # Verifica se chegou ao enésimo termo
    if enesimo_termo == 0:
        # Pergunta se deseja adicionar mais termos
        pergunta = str(input('Deseja adicionar mais termos? S/N')).strip().upper()

        # Valida a resposta, solicitando novamente caso seja inválida
        while pergunta not in 'SsNn':
            print('Resposta inválida!')
            pergunta = str(input('Deseja adicionar mais termos? S/N')).strip().upper()

        # Se a resposta for 'S', solicita a quantidade de termos adicionais
        if pergunta == 'S':
            print('Quantos?')
            termos_adicionais = int(input(''))

            # Calcula o novo enésimo termo
            enesimo_termo = razao * termos_adicionais
            print(f'Exibindo mais {termos_adicionais} termos.')
            resposta = False
        # Se a resposta for 'N', encerra o programa
        elif pergunta == 'N':
            print('OK. Encerrando...')
            resposta = True

# Exibe a quantidade total de termos mostrados
print(f'Foram mostrados {termos_exibidos} termos.')



