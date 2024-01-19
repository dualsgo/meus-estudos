# Curso Python #22 - Módulos e Pacotes

# Modularização:
# Surgiu no início da década de 60
# Sistemas ficando cada vez maiores
# Foco: dividir um programa grande
# Foco: aumentar a legibilidade
# Foco: facilitar a manutenção

from pacote import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O factorial de {num} é {fat}.')
dob = uteis.dobro(num)
print(f'O dobro de {num} é {dob}.')
tri = uteis.triplo(num)
print(f'O triplo de {num} é {tri}.')

# Vantagens:
# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilização em outros projetos


# Pacotes: