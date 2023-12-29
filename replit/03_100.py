# Concatenar: Sim, palavra grande.
# Tudo o que realmente significa é combinar texto (lembre-se, texto é chamado de cadeia de caracteres) e variáveis juntas em frases únicas! 😲🤯
# Você pode fazer sua entrada e saída ficar super bonita agora! 🥳

meuNome = input("Qual é o seu nome? ")
meuAlmoço = input("O que você vai almoçar? ")
print(meuNome, "vai devorar", meuAlmoço, "muito em breve!")

# Você acabou de fazer uma frase completa, certo? Mas como funcionava?
# Acontece que print() tem um superpoder. Podemos dar-lhe quantas coisas diferentes imprimirmos quanto quisermos. Tudo o que precisamos fazer é colocar uma vírgula entre cada coisa diferente

numero = input("Me dê um número: ")
grupo = input("Me dê um substantivo coletivo para um grupo de coisas: ")
coisa = input("Me dê o nome de algo estranho ou extravagante: ")
print("Não, eu não acho que", numero, "é um", grupo, "de", coisa, ". Isso é apenas estranho.")

# Você pode combinar quantas coisas quiser na ordem que quiser, desde que estejam separadas por essa vírgula!

# Erros comuns
"""
seuNome = input("Nome: ")
queAno = input("Em que ano estamos?: ")
print(seuNome "acha que estamos em" queAno)

# Um erro fácil de cometer é esquecer uma ou mais vírgulas.
# Lembre-se de que você precisa de uma vírgula entre cada objeto diferente que está tentando imprimir.
# Sem a vírgula, o computador fica confuso e mostra um erro

  Arquivo "main.py", linha 3
    print(seuNome "acha que estamos em" queAno)
                   ^
Erro de Sintaxe: sintaxe inválida
"""

seuNome = input("Nome: ")
queAno = input("Em que ano estamos? ")
print("seuNome, acha que estamos em, queAno")  # Outro erro comum ocorre quando você envolve a coisa inteira entre aspas.(".., .., .. ")
# Isso realmente funciona, mas não faz exatamente o que você quer.
# Tudo em é impresso literalmente.(".., .., .. ")
# Como os nomes das variáveis estão entre aspas, é literalmente imprimir os nomes em vez do conteúdo. A única coisa entre aspas deve ser as cadeias literais
print(seuNome, "acha que estamos em", queAno)
