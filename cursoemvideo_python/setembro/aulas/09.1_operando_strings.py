# MIMO - Operações com strings

# Dividindo strings (.split()) - Somos capazes de dividir strings codificando .split() após o nome da variável. Assim, obtemos uma lista de elementos dependendo do separador escolhido.

nome = "Maycon Douglas Barros da Silva"
# A variável 'nome' recebe um nome completo como valor.
lista_nome = nome.split()
print(lista_nome)  # Exibe ['Maycon', 'Douglas', 'Barros', 'da', 'Silva']

# As strings são separadas com espaço por padrão, mas podemos especificar um separador diferente entre os parênteses.
usuarios = "Maycon, Douglas, Jonas, Roberto"
lista_usuarios = usuarios.split(", ")
print(lista_usuarios)  # Exibe ['Maycon', 'Douglas', 'Jonas', 'Roberto']

# Atualizando uma string (.replace()) - Às vezes, queremos atualizar os dados dentro de uma string sem criar uma nova variável para isso. Podemos substituir parte de uma string armazenada em uma variável codificando o nome da variável seguido pela instrução .replace().

# Dentro dos parênteses, colocamos primeiro o que desejamos substituir, separamos com uma vírgula e, em seguida, colocamos o que desejamos incluir.
exemplo = "Este é um teste."
print(exemplo)  # Exibe 'Este é um teste.'

# Atribuímos o valor atualizado a uma nova variável em vez de redeclarar.
exemplo2 = exemplo.replace("teste", "exemplo")
print(exemplo2)  # Exibe 'Este é um exemplo.'
# O valor da variável original não muda!
print(exemplo)  # Ainda exibe 'Este é um teste.'
# Todas as ocorrências serão atualizadas.
