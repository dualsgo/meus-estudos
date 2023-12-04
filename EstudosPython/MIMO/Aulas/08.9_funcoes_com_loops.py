# MIMO - 08 - Funções
# 08.9 - Funções com loops

# Intervalos como range(3) nos dizem quantas vezes o loop for é executado, como três vezes nesse caso

def progress():
    for i in range(1, 4):
        print(f'Download file {i} out of 3')

progress()

# Para reutilizar um loop for com qualquer intervalo, passamos um parâmetro entre range()

def progress(files):
    for i in range(files):
        print(f'Download file {i+1} out of  {files}')

# O valor que passamos ao chamar a função é armazenado no parâmetro e depois usado como intervalo
qt_files = int(input('Files = '))

progress(qt_files)

# Para reutilizar um loop que itera pro uma lista, podemos aninhá-lo em uma função, como este loop for
# Para iterar com qualquer tipo de lista, usamos o parâmetro da função em vez de uma lista fixa.
def metade_do_preco(carrinho):
    for preco in carrinho:
        print(f'Novo preço: {preco/2}')

lista_carrinho = [5, 20, 8]

# Ao percorre a lista no parâmetro, podemos chamar a função com qualquer lista, como lista_carrihno aqui
metade_do_preco(lista_carrinho)



