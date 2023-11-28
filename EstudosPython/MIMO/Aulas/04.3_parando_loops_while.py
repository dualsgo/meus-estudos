# MIMO - 04 - Loops

# 4.3 - Parando loops while

# Até agora aprendemos como criar um loop while, agora vamos nos concentrar em como impedi-lo de fazer um loop infinito.

# Para parar um loop, começamos criando uma variável fora do loop.
continuar = True
while continuar: # É o mesmo que comparar se continuar == True
    print('De novo...')

    continuar = False

    print('Só dessa vez.')

# Dentro do bloco de código, paramos o loop definindo continuar como False

# O loop executa todo o seu bloco porque continuar é True no início, mas não é executado novamente se definimos continuar como False

