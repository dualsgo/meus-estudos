"""Desafio 062 - Super Progressão Aritimética v.3.0 (Aula 01 a 14): Melhore o desafio 061, perguntando o usuário se ele quer mostrar maus alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
"""
# Ler o primeiro termo da PA e a razão
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = primeiro
decimo = primeiro + (10 - 1) * razao
total = 10
# Mostrar os 10 primeiros termos
while contador <= decimo:
    print(contador, end=', ')
    contador += razao
    if contador == decimo + razao:
        print('\nDeseja ver mais termos? S/N')
        resposta = str(input('')).strip().upper()
        if resposta in 'Ss':
            termos = int(input('Quantos?'))
            decimo = contador + (termos - 1) * razao  # Atualiza o décimo termo
            total += termos
            if termos == 0:
                print('Obrigado por usar!')
        elif resposta in 'Nn':
            print('Obrigado por usar!')
        else:
            print('Resposta inválida!')
            resposta = str(input('')).strip().upper()
print(f'Finalizando com {total} termos')
