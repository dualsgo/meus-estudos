"""Desafio 009 - Tabuada (Aula 01 a 07): Faça um programa que leia um número inteiro qualquer e mostre a sua dabuada."""

# Passo 1: Ler o número - Para isso armazenamos o valor recebido utilizando uma função input em uma variavel
print("""
=======================
=    T A B U A D A    =
=======================
""")
print('Digite um número para ver sua tabuada:')
numero = int(input(''))
# Passo 2: Mostrar a tabuada desse número até 10 - Nesse exercicio exibiremos todos os resultados na mesma string formatada.
print(f"""
-----------------------------------------------
        \033[7;mA tabuada de {numero} até 10 é:\033[m
-----------------------------------------------
\033[1;31m{numero}\033[m X  \033[1;34m0\033[m = \033[1;32m{numero * 0:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m1\033[m = \033[1;32m{numero * 1:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m2\033[m = \033[1;32m{numero * 2:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m3\033[m = \033[1;32m{numero * 3:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m4\033[m = \033[1;32m{numero * 4:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m5\033[m = \033[1;32m{numero * 5:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m6\033[m = \033[1;32m{numero * 6:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m7\033[m = \033[1;32m{numero * 7:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m8\033[m = \033[1;32m{numero * 8:2}\033[m
\033[1;31m{numero}\033[m X  \033[1;34m9\033[m = \033[1;32m{numero * 9:2}\033[m
\033[1;31m{numero}\033[m X \033[1;34m10\033[m = \033[1;32m{numero * 10:2}\033[m 
-------------------------------------------------
""")
