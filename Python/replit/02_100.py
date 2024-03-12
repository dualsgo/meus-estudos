# Recebendo a entrada do usuário
# Enquanto o comando print() exibe os dados, o comando input() recebe os dados

# Usamos variáveis para armazenar os dados
# Nomeando variáveis
# Você pode dar a uma variável o nome que quiser, mas não pode usar espaços. Você pode usar:
# underscores_between_words
# camelCaseToMakeItEasierToRead

# Agora temos três variáveis:
meuNome = input("Qual é o seu nome? ")  # meuNome tem o nome do usuário nele
minhaIdade = input("Quantos anos você tem? ")  # minhaIdade está armazenando sua idade
print("Caramba, isso é REALMENTE VELHO")
replit = input("Você gosta do Replit? ")  # replit está armazenando seus sentimentos sobre este site incrível.
print("CLARO QUE SIM!")

# Imprimindo uma variável
# Você pode imprimir sua variável usando e o nome usado para sua variável em seu comando. Lembre-se das três variáveis que acabamos de criar

print()  # se não houver nada dentro do () então uma linha em branco é adicionada para um pouco de espaço
print("Então, você é")  # se houver texto dentro do () texto é impresso
print(meuNome)  # se houver uma variável dentro do () o valor é impresso
print("e tem a idade madura de")
print(minhaIdade)
print("e claramente acha que o Replit é, incrível. Certo?")
print(replit)

"""
Erro de Sintaxe
minha variavel = input("QUEM VAI LÁ? ")
print(minha variavel)

  Arquivo "main.py", linha 1
    minha variavel = input("QUEM VAI LÁ? ")
       ^
Erro de Sintaxe: sintaxe inválida

# Percebeu o espaço no nome da variável? Nós nunca colocamos espaços em nomes de variáveis - isso só confunde o pobre computador!

minhaVovó = input("Como está sua avó? 😘 ")
print(minhavovó)

Como está sua avó? 😘 bem
Rastreamento (mais recente chamada por último):
  Arquivo "main.py", linha 2, em <module>
    print(minhavovó)
NomeError: name 'minhaVovó' is not defined

# O que estamos tentando imprimir NÃO é o mesmo que definimos em primeiro lugar. A capitalização de minhaVovó é diferente de minhavovó
# Isso também é importante quando você tenta imprimir uma variável que ainda não criou. Você deve SEMPRE criar a variável ANTES de imprimi-la.
"""

# Você não receberá um erro deste, mas a saída não fará muito sentido...
meuAlmoço = input("O que você vai almoçar? ")
print("Hmm, parece que você realmente deveria pedir")
print('meuAlmoço')  # Você tentou imprimir uma variável, mas adicionou entre aspas!
print("o mais rápido possível!")

# Lembre-se: as citações literalmente imprimirão o que você colar nelas.
# Nesse caso, ele está imprimindo o nome da variável em vez do conteúdo da variável.
# Se você quer o conteúdo, então você NÃO USE ASPAS.

print("Definitivamente não é um Golpe de Phishing")
print()
meuNome = input("Seu Nome")
print("Obrigado por fazer login")
print(meuNome)
numeroCartao = input("Qual é o número do seu cartão de crédito?")
print("Obrigado, eu definitivamente não vou colocar")
print(numeroCartao)
print("na Amazon e pedir algo estranho")
print()
print("Prometo")
nomeSolteira = input("Qual é o nome de solteira da sua mãe? ")
print()
print("Legal, eu só queria saber que")
print(nomeSolteira)
print("era o nome de solteira da sua mãe. Não porque o banco pediu ou algo assim, honesto.")

# Desafio 02

nome = input('Digite o seu nome: ')

comida_favorita = input('Qual é a sua comida favorita? ')

musica_favorita = input('Qual é a sua música favorita? ')

onde_mora = input('Onde você mora? ')

print(f'Você é {nome}')

print(f"Você provavelmente está com fome de {comida_favorita}")

print(f"e com certeza está curtindo {musica_favorita}")

print(f'Você mora em {onde_mora}')
