
lista = []
lista_par = []
lita_impar = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
# Lê o número
# Adiciona o número na lista
# Pergunta se quer continuar
# Se for 'N' para imediatamente o programa (Aqui está o erro)
# Se for qualquer outra resposta (Pois não tem validação para ser especificamente 'S') ele avalia se é PAR e adiciona a lista de pares, se não adiciona a lista de ímpares e recomeça o loop.

# Se a resposta for 'N', o seu código para antes de incluir o valor em uma das listas. Você só precisa trocar a ordem


    if n % 2 == 0:
        lista_par.append(n)
    else:
        lita_impar.append(n)

	resposta = str(input('Quer continuar? [S/N]')).upper()
	if resposta in 'N':
		break

lista.sort()
lista_par.sort()
lita_impar.sort()

print(f'A lista completa é : {lista}')
print(f'Os pares da lista são: {lista_par}')
print(f'Os impares da lista são: {lita_impar}')