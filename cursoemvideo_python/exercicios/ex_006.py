"""Desafio 006 - Dobro, Triplo, Raiz Quadrada (Aula 01 a 07): Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

# Passo 1: Ler o número fornecido pelo usuário: Para isso utilizamos uma variável para armazenar esse valor que será fornecido através de uma função input() convertida para valor int.
print("""
\033[7mDOBRO, TRIPLO E RAIZ QUADRADA\033[m  
""")
print('Digite um número:')
numero = int(input(''))
# Passo 2: Mostrar o dobro, tripo e raiz quadrada: Para melhor entendimento iremos criar uma variável para cada ação.

# Para chegar ao dobro basta multiplicar o valor fornecido por 2
dobro = numero * 2
# Para chegar ao triplo basta multiplicar o valor por 3
triplo = numero * 3
# Para chegar a raiz quadrada devemos elevar o valor a meio (1/2). A divisão retorna um valor float, nesse caso para efeito visual convertemos para int
raiz_quadrada = numero ** (1/2)
# Por fim basta exibir os resultados por meio da função print
print(f"""
\033[1;31mVocê digitou o número {numero}\033[m

\033[1;32mO dobro de {numero} é {dobro}.\033[m
\033[1;33mO triplo de {numero} é {triplo}.\033[m
\033[1;34mA raiz quadrada de {numero} é {raiz_quadrada:.2f}.\033[m
""")
