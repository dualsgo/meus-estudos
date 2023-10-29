from random import randint

numeros = []

while len(numeros) < 5:
    entrada = input(
        'Digite um número ou pressione Enter para adicionar um número aleatório: ')
    if entrada:
        numeros.append(entrada)
    else:
        numeros.append(str(randint(0, 999)))

print(
    f"\n\033[7mVocê digitou os seguintes números:\033[m \033[1m{', '.join(numeros)}\033[m.")

print(f"""
\033[7mO menor número da lista é:\033[m \033[1m{min(numeros)}\033[m.
\033[7mO maior número da lista é:\033[m \033[1m{max(numeros)}\033[m.
""")

# EXTRA - Poderíamos ordenar a lista e mostrar o primeiro índice e o último
numeros.sort()
print(f"""A lista em ordem crescente é: {', '.join(numeros)}
O menor número é o {numeros[0]} e o maior é {numeros[-1]}""")
