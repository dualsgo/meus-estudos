"""Desafio 026 - Título (Aula 01 a 09): Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece pela primeira vez.
- Em que posição aparece pela última vez.
"""
# Passo 1: Ler a frase - A frase será obtida atráves da função input que foi atribuída a uma variável. O input recebe um tratamento prévio com strip para eliminar espaços desnecessário no início e no final
frase = str(input('Digite uma frase: ')).strip()

# Passo 2: Usar os métodos para chegar aos resultados

# Para contabilizar a quantidade de ocorrências usamos count()
qtde_a = frase.lower().count('a')  # Usando lower() para considerar 'A' e 'a' como a mesma letra.

# Para encontrar a primeira ocorrência, usamos find() que iniciará a busca da esquerda para direita
primeira = frase.lower().find('a') + 1  # Adicionando 1 para mostrar a posição correta (não começando em 0).

# Para encontrar a última ocorrência, usamos rfind() que iniciará a busca da direita para esquerda
ultima = frase.lower().rfind('a') + 1  # Usando rfind() para encontrar a última ocorrência.

print(f"""
A quantidade de ocorrências da letra 'a' na frase '{frase}' é: {qtde_a}.
A primeira ocorrência da letra 'a' na frase '{frase}' está na posição: {primeira}.
A última ocorrência da letra 'a' na frase '{frase}' está na posição: {ultima}.""")
