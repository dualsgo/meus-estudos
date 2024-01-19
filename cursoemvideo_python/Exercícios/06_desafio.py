# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada - Aula 00 até 07 - Mundo 1
# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Tarefa 1: Ler um número
numero = int(input('Digite um número: '))

# Tarefa 2: Mostrar o seu dobro, triplo e raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'Você digitou o número {numero}.')
print(f'O dobro de {numero} é {dobro}, e o triplo {triplo}.')
print(f'A raiz quadrada de {numero} é aproximadamente {raiz:.2f}.')