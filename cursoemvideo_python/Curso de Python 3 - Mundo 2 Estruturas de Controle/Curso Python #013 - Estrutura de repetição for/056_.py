# Fazer com dicionários

# Lista para armazenar as informações das pessoas
lista_pessoas = []

# Loop para coletar informações de três pessoas
for i in range(3):
    pessoa = {
        'nome': input('Nome: ').strip().title(),
        'idade': int(input('Idade: ')),
        'sexo': input('Sexo: ').strip().upper()
    }
    # Adiciona o dicionário da pessoa à lista
    lista_pessoas.append(pessoa)

# Exibe a lista de pessoas
print("Informações das pessoas:")
for pessoa in lista_pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")