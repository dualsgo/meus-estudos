faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "lira@gmail.com"

# maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)
# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# "@"
print(email_cliente.find("@")) # -1 quando não encontrar

# tamanho do texto
print(len(email_cliente))

# pegar um caractere
print(email_cliente[4])

print(email_cliente[-4])

# pegar um pedaço do texto
print(email_cliente[4:])

# trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "joao lira"
# trabalhar com nomes
print(nome.capitalize())
print(nome.title())

# pegar o servidor do email
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

# pegar o 1º nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]

# pegar o sobrenome
sobrenome = nome[posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)

# casos especiais - formatações numéricas em texto
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro:.0%}")