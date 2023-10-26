"""Desafio 022 - Título (Aula 01 a 09): Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras MAIÚSCULAS.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

# Passo 1: Ler o nome completo - Armazenamos o valor atribuindo a uma variável a função input(), assim o valor da variável será aquele que o usuário digitar
print('\033[1;31;40mDigite o seu nome completo!\033[m')
nome = str(input(''))  # Um input retorna um valor do tipo string por padrão
# Os espaços inúteis podem ser removidos nessa instância com strip, mas nesse exercício será feito posteriormente

# Passo 2: Tratar a string - Para fins didáticos e facilitar o entendimento vou armazenar cada resultado em um avariável

em_maiusculas = nome.upper()
print(f'O nome digitado em MAIÚSCULAS: \033[1;31m{em_maiusculas}\033[m')
em_minusculas = nome.lower()
print(f'O nome digitado em minusculas: \033[1;32m{em_minusculas}\033[m')

# Para saber a quantidade de letras ao total, desconsiderando espaços removemos os inúteis com strip()
sem_espacos = nome.split()
# Depois de remover os espaços inúteis, usamos split para separar as palavras em índices individuais
# Depois usamos join para unir todos os indices envolvidos por len() para exibir a quantidade total de caracteres.

# Obs - Atentar-se ao uso de aspas diferentes para delimitar a string e o metodo join
print(
    f'A quantidade de caracteres do nome digitado, desconsiderando os espaços é: \033[1;33m{len("".join(sem_espacos))}.\033[m')

# Para saber quantas letras tem o primeiro nome, após usar split, envolvemos a variável indicando o primeiro indice envolta do método len()
print(
    f'A quantidade de letras do primeiro nome é: \033[1;34m{len(sem_espacos[0])}\033[m.')
