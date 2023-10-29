"""Desafio 026 - Primeira e última ocorrência de uma string (Aula 01 a 09): Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece pela primeira vez.
- Em que posição aparece pela última vez.
"""
# Passo 1: Ler a frase - A frase será obtida atráves da função input que foi atribuída a uma variável. O input recebe um tratamento prévio com strip para eliminar espaços desnecessário no início e no final
print('\033[1;43mAnalizando frases!\033[m')
frase = str(input('Digite uma frase: ')).strip()

# Passo 2: Usar os métodos para chegar aos resultados

# Para contabilizar a quantidade de ocorrências usamos count()
# Usando lower() para considerar 'A' e 'a' como a mesma letra.
qtde_a = frase.lower().count('a')

# Para encontrar a primeira ocorrência, usamos find() que iniciará a busca da esquerda para direita
# Adicionando 1 para mostrar a posição correta (não começando em 0).
primeira = frase.lower().find('a') + 1

# Para encontrar a última ocorrência, usamos rfind() que iniciará a busca da direita para esquerda
# Usando rfind() para encontrar a última ocorrência.
ultima = frase.lower().rfind('a') + 1

print(f"""
\033[31mA quantidade de ocorrências da letra 'a' na frase '{frase}' é: \033[m\033[1m{qtde_a}.\033[m
\033[32mA primeira ocorrência da letra 'a' na frase '{frase}' está na posição: \033[m\033[1m{primeira}.\033[m
\033[33mA última ocorrência da letra 'a' na frase '{frase}' está na posição: \033[m\033[1m{ultima}.\033[m""")
